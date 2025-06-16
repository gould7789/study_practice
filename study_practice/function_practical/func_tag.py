# HTML 태그 이름과 내용을 매개변수로 받아, 해당 태그로 감싸진 HTML 요소를 반환하는 함수 작성

def wrap_in_tag(tag, word):
    print(f"<{tag}>{word}<{tag}>")

wrap_in_tag("p", "hello")
wrap_in_tag("b", "world")