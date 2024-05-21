import sqlite3
con = sqlite3.connect('youtube_video')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name Text NOT NULL,
               time Text NOT NULL
    )
''')

def all_videos():
    cursor.execute("select * from videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("insert into videos(name,time) values(?,?) ",(name,time))
    con.commit()
def update_video(video_id,new_name,new_time):
    cursor.execute("update videos set name=?,time=? where id=? ",(new_name,new_time,video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("delete from videos where id=? ",(video_id,)) #never se single variable without comma after it
    con.commit()


def main():
    while True:
        print("YOUTUBE MANAGER | CHOOSE AN OPTION")
        print("1. List all youtube videos")
        print("2. Add a youtbe videos")
        print("3. Update a youtube videos details")
        print("4. Delete a youtube videos")
        print("5. Exit the app")
        choice = input("Enter your choice : ")

        if choice == '1':
            all_videos()
        elif choice == '2':
            name = input("enter the videos name : ")
            time = input("enter the video time : ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("enter the video id to update: ")
            name = input("enter the videos name : ")
            time = input("enter the video time : ")
            update_video(video_id,name, time)
        elif choice == '4':
            video_id = input("enter the video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("invalid choice")
    con.close()
            

if __name__ == '__main__':
    main()


