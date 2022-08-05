from helper import *

def display_skill_videos(token):
    conn = db_connection()
    c = conn.cursor()
    
    video_list = []

    if token == str(-1) or not validate_token(conn, token):
        video_list = get_skill_videos(conn, -1)
    else:
        user = decode_token(conn, token)
        if user["is_contributor"]:
            video_list = get_skill_videos(conn, -1)
        else:
            video_list = get_skill_videos(conn, user["user_id"])
    
    c.close()
    
    return video_list

def contributor_skill_videos(user):
    conn = db_connection()
    c = conn.cursor()

    contributor_id = user["user_id"]
    video_list = []

    c.execute("SELECT * FROM SkillVideos WHERE contributor_id = ?", [contributor_id])
    videos = c.fetchall()
    for row in videos:
        prefix = "https://www.youtube.com/"
        c.execute("SELECT * FROM Contributors WHERE id = ?", [contributor_id])
        creator_details = c.fetchone()
        video_list.append({"id" : row[0], "title" : row[2], "url" : prefix + row[3], "creator": creator_details[2], "creator_profile_pic" : creator_details[4]})
    
    c.close()

    return video_list

def ruser_skill_videos(user):
    conn = db_connection()
    c = conn.cursor()

    user_id = user["user_id"]

    c.execute("SELECT skill_video_id FROM SkillVideoSaves WHERE ruser_id = ?", [user_id])

    videos = c.fetchall()
    
    if videos is None:
        return{"video_list" : []}

    video_list = []
    for v in videos:
        c.execute("SELECT * FROM SkillVideos WHERE id = ?", [v[0]])
        row = c.fetchone()
        c.execute("SELECT * FROM Contributors WHERE id = ?", [row[1]])
        creator_details = c.fetchone()
        prefix = "https://www.youtube.com/"
        video_list.append({"id" : row[0], "title" : row[2], "url" : prefix + row[3], "creator": creator_details[2], "creator_profile_pic" : creator_details[4]})
    
    return video_list

def add_skill_videos(user_details, video_name, url):
    conn = db_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM skillVideos ORDER BY id DESC LIMIT 1")
    video_id = c.fetchone()[0]
    video_id = video_id + 1

    c.execute("INSERT INTO SkillVideos VALUES (?, ?, ? ,?)", [video_id, user_details["user_id"], video_name, url])
    conn.commit()
    c.close()

    return {}

def validate_uploader(user_details, video_id):
    conn = db_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM SkillVideos WHERE contributor_id = ? AND id = ?", [user_details["user_id"], video_id])
    if c.fetchone() is None:
        return -1
    
    return 1


def delete_skill_videos(video_id):
    conn = db_connection()
    c = conn.cursor()

    c.execute("DELETE FROM SkillVideos WHERE id = ?", [video_id])

    conn.commit()

    return {}

def skill_videos_saved(user_details, video_id):
    conn = db_connection()
    c = conn.cursor()

    user_id = user_details["user_id"]
    if has_saved_video(conn, video_id, user_id):
        c.execute("DELETE FROM skillVideoSaves WHERE skill_video_id = ? AND ruser_id = ?", [video_id, user_id])
    else:
        c.execute("INSERT INTO SkillVideoSaves VALUES (?, ?)", [user_id, video_id])
    
    conn.commit()

    return {}

def search_skill_videos(search_string):
    conn = db_connection()
    c = conn.cursor()

    video_list = []

    c.execute("SELECT * FROM skillVideos WHERE LOWER(title) LIKE ?", ['%'+search_string+'%'])
    videos = c.fetchall()
    for v in videos:
        c.execute("SELECT * FROM Contributors WHERE id = ?", [v[1]])
        creator_details = c.fetchone()
        prefix = "https://www.youtube.com/"
        video_list.append({"id" : v[0], "title" : v[2], "url" : prefix + v[3], "creator": creator_details[2], "creator_profile_pic" : creator_details[4]})

    return video_list


