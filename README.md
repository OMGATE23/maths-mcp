# maths-mcp

Does all the cool maths related stuff for your LLM. Goal is to support all the maths tools we can support

Run the following command:

```
maths-mcp --rounded
```

# Video Search Application

A Streamlit web application that allows you to upload videos and search through their content using VideoDB's powerful video processing capabilities.

## Features

- Upload videos from YouTube URLs or direct video links
- Automatic indexing of both spoken words and visual content
- Search through videos using natural language queries
- Support for both semantic and keyword search
- Search in either spoken content or visual scenes
- View search results with timestamps and descriptions
- Manage your video library

## Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Get your VideoDB API key from [VideoDB Console](https://console.videodb.io)

3. Set your VideoDB API key as an environment variable:

```bash
export VIDEODB_API_KEY="your-api-key-here"
```

4. Run the application:

```bash
streamlit run app.py
```

## Usage

1. **Upload Videos**:

   - Use the sidebar to enter a YouTube URL or video link
   - Click "Upload Video" to add it to your library
   - The video will be automatically indexed for both spoken content and visual scenes

2. **Search Videos**:

   - Choose your search type (Semantic or Keyword)
   - Select the content type to search in (Spoken Word or Scene)
   - Enter your search query
   - Click "Search" to find relevant video segments

3. **View Results**:

   - Watch the compiled video of matching segments
   - Expand individual segments to see timestamps and transcripts
   - Browse your video library in the bottom section

4. **Manage Library**:
   - View all uploaded videos
   - See video duration and details
   - Delete videos when no longer needed

## Notes

- The application uses VideoDB's AI-powered indexing to process videos
- Indexing may take some time depending on video length
- Semantic search provides more natural language understanding
- Scene search can find visual content and actions
- All videos are stored in your VideoDB collection

## Support

For any issues or questions:

- Check the [VideoDB Documentation](https://docs.videodb.io)
- Join the [VideoDB Discord](https://discord.gg/py9P639jGz)
- Visit [videodb.io](https://videodb.io)
