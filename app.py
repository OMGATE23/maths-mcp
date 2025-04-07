import os
import streamlit as st
from videodb import connect, SearchType, IndexType, MediaType

# Initialize VideoDB connection
def init_videodb():
    api_key = os.getenv("VIDEODB_API_KEY")
    if not api_key:
        st.error("Please set the VIDEODB_API_KEY environment variable")
        st.stop()
    return connect(api_key=api_key)

# Main application
def main():
    st.title("🎥 Video Search Application")
    
    # Initialize VideoDB
    conn = init_videodb()
    collection = conn.get_collection()

    # Sidebar for uploading videos
    with st.sidebar:
        st.header("Upload Video")
        video_url = st.text_input("Enter YouTube URL or video link")
        
        if st.button("Upload Video"):
            if video_url:
                with st.spinner("Uploading video..."):
                    try:
                        video = collection.upload(url=video_url)
                        st.success(f"Video '{video.name}' uploaded successfully!")
                        
                        # Index the video for both spoken words and scenes
                        with st.spinner("Indexing video content..."):
                            video.index_spoken_words()
                            video.index_scenes(prompt="Describe the scene in detail, including objects, actions, and setting.")
                            st.success("Video indexed successfully!")
                    except Exception as e:
                        st.error(f"Error uploading video: {str(e)}")

    # Main content area for searching
    st.header("🔍 Search Videos")
    
    # Search options
    search_type = st.selectbox(
        "Search Type",
        ["Semantic", "Keyword"],
        format_func=lambda x: f"{x} Search"
    )
    
    index_type = st.selectbox(
        "Content Type",
        ["Spoken Word", "Scene"],
        format_func=lambda x: f"Search in {x} content"
    )
    
    # Search query
    query = st.text_input("Enter your search query")
    
    if st.button("Search"):
        if query:
            with st.spinner("Searching..."):
                try:
                    # Convert selection to enum values
                    search_type_enum = SearchType.semantic if search_type == "Semantic" else SearchType.keyword
                    index_type_enum = IndexType.spoken_word if index_type == "Spoken Word" else IndexType.scene
                    
                    # Perform search
                    results = collection.search(
                        query=query,
                        search_type=search_type_enum,
                        index_type=index_type_enum
                    )
                    
                    # Display results
                    if results:
                        st.subheader("Search Results")
                        stream_url = results.generate_stream()
                        st.video(stream_url)
                        
                        # Display individual shots/segments
                        shots = results.get_shots()
                        if shots:
                            st.subheader("Found Segments")
                            for i, shot in enumerate(shots, 1):
                                with st.expander(f"Segment {i} ({shot.start:.1f}s - {shot.end:.1f}s)"):
                                    st.write(shot.text)
                    else:
                        st.info("No results found for your query.")
                except Exception as e:
                    st.error(f"Error performing search: {str(e)}")
        else:
            st.warning("Please enter a search query.")

    # Display all videos in collection
    st.header("📚 Video Library")
    videos = collection.get_videos()
    if videos:
        for video in videos:
            with st.expander(f"Video: {video.name}"):
                st.write(f"Duration: {video.length:.1f}s")
                if st.button("Delete Video", key=f"delete_{video.id}"):
                    try:
                        video.delete()
                        st.success("Video deleted successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error deleting video: {str(e)}")
    else:
        st.info("No videos in the library. Upload some videos to get started!")

if __name__ == "__main__":
    main() 