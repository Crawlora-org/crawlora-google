import { GoogleClient } from "../src/index.js";

const client = new GoogleClient({ apiKey: "test-key" });
void client.financeAnalystArticles({"quote": "sample"});
void client.request("google-finance-analyst-articles", {"quote": "sample"});
const streamResponse: Promise<Response> = client.request("google-finance-analyst-articles", {"quote": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("google-finance-analyst-articles", {"quote": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.financeAnalystArticles({"quote": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("google-finance-analyst-articles", {"quote": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("google-finance-analyst-articles", {"quote": "sample"}, { responseType: "text" });
void rawText;


void client.financeMarketsEarnings();
void client.request("google-finance-markets-earnings");
// @ts-expect-error The selected operation requires its documented params.
void client.financeAnalystArticles();
