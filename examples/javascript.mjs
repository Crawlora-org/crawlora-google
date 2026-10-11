import { GoogleClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new GoogleClient({ apiKey });

  const news = await client.news({ q: "artificial intelligence" });
  console.log("news", news);
  const mapSearch = await client.mapSearch({ mapSearchOption: {"keyword": "coffee shops in Seattle", "country": "us", "language": "en"} });
  console.log("mapSearch", mapSearch);
  const trendsTrending = await client.trendsTrending({ geo: "US" });
  console.log("trendsTrending", trendsTrending);
