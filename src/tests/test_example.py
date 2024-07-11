# def func(x):
#     return x + 1
#
#
# def test_answer():
#     assert func(4) == 5
#
# def test_answer_2():
#     assert func(4) == 6

# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "y" in x,"some error test message"
#
# def test_two(self):
#     x = "hello"
#     assert hasattr(x, "check")


# def test_sum_2_obj_str():
#     assert "a" + "b" == "ab"
#
#
# def test_sum_2_obj_int():
#     assert 2 + 4 == 6
#
#
# def test_sum_3_obj_int(some_fixture_1,some_fixture_2):
#     assert [1, 2, 3, 4] == some_fixture_1
#     assert 5 + 14 == 19


#
# def summa(a, b):
#     return a + b
#
#
# def test_sum_2_obj_int_str():
#     with pytest.raises(TypeError) as error:
#         summa("1", 2)


# @pytest.mark.parametrize("value_1,value_2,expected",
#                          [
#                              (3, 5, 8),
#                              (2, 4, 6),
#                              (6, 7, 13)]
#                          )
#
# def test_first(some_fixture_1):
#     assert 1 == 1




def test_read_main():
    response = client.get("/books/books")
    import pdb;pdb.set_trace()
    assert response.status_code == 200
    assert response.json() == {
        "DB_PORT": "some port",
        "DB_HOST": "some host",
    }