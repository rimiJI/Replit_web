import turtle

# 화면 설정
screen = turtle.Screen()
screen.title("Turtle Control")
screen.bgcolor("white")

# 거북이 객체 생성
t = turtle.Turtle()
t.shape("turtle")
t.color(0.0, 0.9, 1)  # 색상을 민트색으로 설정

# 이동 함수 정의
def move_up():
    t.setheading(90)
    t.forward(20)

def move_down():
    t.setheading(270)
    t.forward(20)

def move_left():
    t.setheading(180)
    t.forward(20)

def move_right():
    t.setheading(0)
    t.forward(20)

def exit_program():
    turtle.bye()  # 프로그램 종료

# 키 바인딩
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(exit_program, "Return")  # 엔터키로 종료

# 메인 루프
screen.mainloop()
