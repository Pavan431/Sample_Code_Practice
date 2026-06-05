import requests
import json

def send_get_request():
    
    response = requests.get(
        "http://216.10.245.166/Library/GetBook.php", params={"AuthorName": "Rahul_Shetty2"}
    )

    """ json_response=response_json.text

    dict_resp= json.loads(json_response)

    print(type(dict_resp)) """

    assert response.status_code == 200

    # assert False if response.text is not None and response.text != ""
    assert response.text, "Response body is empty"

    data_list = response.json()

    # validate the response should be valid json array
    assert isinstance(data_list, list), "Data does not contain list"
    """ Validate the structure of json like:
        1.No field should be missing
        2.Field names should be consistent (no typos)
        3.Data types should match expected """

    fields = ["book_name", "isbn", "aisle"]
    for book in data_list:
        # print(book.keys())
        for data in book:
            assert isinstance(data, str), "Data is not in expected format"
        for field in fields:
            if field not in book:
                print(book, f"{field} is missing")


    # Find the duplicate book records
    first_seen = set()
    second_seen = set()
    for book in data_list:
        key1 = (book["book_name"], book["isbn"], book["aisle"])
        key2 = (book["book_name"], book["aisle"])
        if key1 in first_seen:
            print("Exact duplicate found", book)

        else:
            first_seen.add(key1)

        if key2 in second_seen:
            print("Duplicate found", book)
        else:
            second_seen.add(key2)


def send_post_request():
    response_addBook= requests.post(
        "http://216.10.245.166/Library/Addbook.php",
        json={
            "name": "Learn Python",
            "isbn": "BGBR234",
            "aisle": "9223",
            "author": "Johnfoe",
        },headers={'Content-Type':'application/json',}
    )
    assert response_addBook.status_code==200
    
    response_json= response_addBook.json()
    print(type(response_json))
    print(response_json)
    if response_json['Msg']== "successfully added":
        print('Test Passed')
    elif response_json['Msg']=='Book Already Exists':
        print('Duplicate entry')
    else:
        raise Exception('API failed')
    ID = response_json['ID']
    return ID
    
    
def send_delete_request(bookid):
    response_delete= requests.post(
            "http://216.10.245.166/Library/DeleteBook.php",
            json={
                "ID": bookid,
            },headers={'Content-Type':'application/json',}
        )
    assert response_delete.status_code==200
    dict_resp= response_delete.json()
    if dict_resp['msg'] =="book is successfully deleted":
        assert True
        print('Deleted the book successfully')
    else:
        raise Exception("API failed in deletion")
        
        
        
        
book_id=send_post_request()
send_delete_request(book_id)
    