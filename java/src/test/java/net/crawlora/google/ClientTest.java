package net.crawlora.google;

import com.sun.net.httpserver.HttpServer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.net.InetSocketAddress;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;

import static org.junit.jupiter.api.Assertions.*;

class ClientTest {
    private HttpServer server;
    private volatile int status = 200;
    private volatile String contentType = "application/json";
    private volatile String body = "{\"ok\":true}";
    private volatile long delayMillis;
    private final AtomicReference<String> seenKey = new AtomicReference<>();
    private final AtomicReference<String> seenUri = new AtomicReference<>();
    private String baseUrl;

    @BeforeEach void startServer() throws Exception {
        server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/", exchange -> {
            seenKey.set(exchange.getRequestHeaders().getFirst("x-api-key"));
            seenUri.set(exchange.getRequestURI().toASCIIString());
            try { if (delayMillis > 0) Thread.sleep(delayMillis); }
            catch (InterruptedException error) { Thread.currentThread().interrupt(); }
            byte[] bytes = body.getBytes(java.nio.charset.StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", contentType);
            exchange.sendResponseHeaders(status, bytes.length);
            try (var output = exchange.getResponseBody()) { output.write(bytes); }
        });
        server.start();
        baseUrl = "http://127.0.0.1:" + server.getAddress().getPort() + "/api/v1";
    }

    @AfterEach void stopServer() { if (server != null) server.stop(0); }

    @Test void platformCatalogIsAnExactAllowlistAndExposesDirectMethod() throws Exception {
        assertEquals(40, Client.OPERATION_IDS.size());
        assertEquals(List.of("google-finance-analyst-articles", "google-finance-chart", "google-finance-classification", "google-finance-company", "google-finance-context", "google-finance-financials", "google-finance-markets-category-news", "google-finance-markets-category-stocks", "google-finance-markets-earnings", "google-finance-markets-featured", "google-finance-markets-headline", "google-finance-markets-indices", "google-finance-markets-movers", "google-finance-markets-top", "google-finance-markets-trending", "google-finance-news", "google-finance-quote", "google-finance-related", "google-finance-search", "google-finance-ticker", "google-jobs", "google-map-place", "google-map-place-photos", "google-map-place-reviews", "google-map-search", "google-news", "google-news-search", "google-suggest", "google-trends-categories", "google-trends-enums", "google-trends-explore", "google-trends-explore-interest-by-region", "google-trends-explore-interest-over-time", "google-trends-explore-related-topics", "google-trends-explore-rising-queries", "google-trends-explore-top-queries", "google-trends-locations", "google-trends-trending", "google-trends-trending-detail", "google-videos"), Client.OPERATION_IDS);
        assertEquals(new java.util.TreeSet<>(Client.OPERATION_IDS), new java.util.TreeSet<>(Client.operations().keySet()));
        assertEquals(Client.OPERATION_IDS.size(), new Client("key").getOperationCount());
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertThrows(IllegalArgumentException.class, () -> client.request("instagram-search", Map.of()));
            Object result = client.request("google-finance-chart", Map.ofEntries(Map.entry("quote", "path /one"), Map.entry("window", "value &/one")));
            assertInstanceOf(Map.class, result);
            assertEquals("test-key", seenKey.get());
            assertTrue(seenUri.get().startsWith("/api/v1/"));
            assertTrue(seenUri.get().contains("%26"), "query values should be URL encoded");
            assertTrue(seenUri.get().contains("path%20%2Fone"), "path values should be URL encoded");
        }
    }

    @Test void directMethodUsesTheSameOperationDispatch() throws Exception {
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            Object result = Client.class.getMethod("financeChart", Map.class).invoke(client, Map.ofEntries(Map.entry("quote", "path /one"), Map.entry("window", "value &/one")));
            assertInstanceOf(Map.class, result);
        }
    }

    @Test void returnsPlainTextWhenTheHostedResponseIsText() {
        contentType = "text/plain; charset=utf-8";
        body = "line one\nline two";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertEquals("line one\nline two", client.request("google-finance-analyst-articles", Map.ofEntries(Map.entry("quote", "sample"))));
        }
    }

    @Test void surfacesHttpErrorsAndTimeouts() {
        status = 422;
        body = "{\"code\":422,\"msg\":\"bad input\"}";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            CrawloraException error = assertThrows(CrawloraException.class,
                    () -> client.request("google-finance-chart", Map.ofEntries(Map.entry("quote", "path /one"), Map.entry("window", "value &/one"))));
            assertEquals(422, error.statusCode());
            assertTrue(error.getMessage().contains("bad input"));
        }
        status = 200;
        delayMillis = 250;
        try (Client client = new Client("test-key", baseUrl, Duration.ofMillis(20))) {
            assertThrows(CrawloraException.class, () -> client.request("google-finance-chart", Map.ofEntries(Map.entry("quote", "path /one"), Map.entry("window", "value &/one"))));
        }
    }

    @Test void rejectsInvalidEnumsAndClosedClientCalls() {
        assertThrows(IllegalArgumentException.class, () -> new Client("key", baseUrl, Duration.ofSeconds(1)).request("google-suggest", Map.ofEntries(Map.entry("q", "sample"), Map.entry("source", "__invalid_java_test_enum__"))));
        Client client = new Client("key", baseUrl, Duration.ofSeconds(1));
        client.close();
        assertThrows(IllegalStateException.class, () -> client.request("google-finance-chart", Map.ofEntries(Map.entry("quote", "path /one"), Map.entry("window", "value &/one"))));
    }
}
