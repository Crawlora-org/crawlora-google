use crawlora_google::{Client, GoogleNewsParams, ModelGoogleNewsResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .google
        .news(GoogleNewsParams {
            q: Some("artificial intelligence".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelGoogleNewsResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
