import json
from create_token import generate_token

def main():
    #rusers schema: ruser_id (int), email (string), username (string), password (string), profile_picture (string)
    rusers_table = []

    #contributors schema: ruser_id (int), email (string), username (string), password (string), profile_picture (string)
    contributors_table = []

    #tokens schema: token (string), user_id (int), is_contributor (bool)
    tokens_table = []

    emails_file = open("./emails.txt", "r")

    passwords_file = open("passwords.txt", "r")

    usernames_file = open("usernames.txt", "r")

    for i in range(0, 180):
        new_email = emails_file.readline().strip()
        new_password = passwords_file.readline().strip()
        new_username = usernames_file.readline().strip()
    
        new_rusers_row = {"ruser_id": i, "email": new_email, "username": new_username, "password": new_password, "profile_picture": ""}

        rusers_table.append(new_rusers_row)
    
    for i in range(180, 200):
        new_email = emails_file.readline().strip()
        new_password = passwords_file.readline().strip()
        new_username = usernames_file.readline().strip()
    
        new_contributors_row = {"contributor_id": i - 180, "email": new_email, "username": new_username, "password": new_password, "profile_picture": ""}

        contributors_table.append(new_contributors_row)

    token_row_1 = {"token": generate_token(rusers_table[15]["email"]), "user_id": rusers_table[15]["ruser_id"], "is_contributor": False}
    token_row_2 = {"token": generate_token(rusers_table[100]["email"]), "user_id": rusers_table[100]["ruser_id"], "is_contributor": False}
    token_row_3 = {"token": generate_token(contributors_table[3]["email"]), "user_id": contributors_table[3]["contributor_id"], "is_contributor": True}
    token_row_4 = {"token": generate_token(contributors_table[7]["email"]), "user_id": contributors_table[7]["contributor_id"], "is_contributor": True}

    tokens_table.append(token_row_1)
    tokens_table.append(token_row_2)
    tokens_table.append(token_row_3)
    tokens_table.append(token_row_4)

    emails_file.close()
    passwords_file.close()
    usernames_file.close()

    fp1 = open("rusers_table.json", "w")
    json.dump(rusers_table, fp1)
    fp1.close()

    fp2 = open("contributors_table.json", "w")
    json.dump(contributors_table, fp2)
    fp2.close()

    fp3 = open("tokens_table.json", "w")
    json.dump(tokens_table, fp3)
    fp3.close()

    return


if __name__ == "__main__":
    main()