from flaskr import youtube

def test_youtube():
    results = youtube.youtube_search("test" , 1)
    assert len(results)== 1
    assert "Test" in results[0]["title"]
    