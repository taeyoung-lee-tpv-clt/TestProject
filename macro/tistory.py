import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk

def post_comment(blog_url, comment):
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')  # ChromeDriver 경로 지정
    driver.get('https://www.tistory.com/auth/login')

    # 로그인
    username = 'your_username'
    password = 'your_password'
    
    user_input = driver.find_element(By.NAME, 'loginId')
    user_input.send_keys(username)
    pass_input = driver.find_element(By.NAME, 'password')
    pass_input.send_keys(password)
    pass_input.send_keys(Keys.RETURN)

    time.sleep(3)  # 로그인 처리가 완료될 때까지 잠시 대기

    # 블로그 글 이동
    driver.get(blog_url)

    # 댓글 입력
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea#comment-textarea'))
    )
    comment_box = driver.find_element(By.CSS_SELECTOR, 'textarea#comment-textarea')
    comment_box.send_keys(comment)

    # 댓글 등록 버튼 클릭
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button.submit-comment')
    submit_button.click()

    time.sleep(3)  # 댓글이 등록될 때까지 잠시 대기
    driver.quit()

def on_submit():
    blog_url = entry_url.get()
    comment = entry_comment.get()
    post_comment(blog_url, comment)

# Tkinter UI 설정
root = tk.Tk()
root.title("Tistory Comment Poster")

tk.Label(root, text="Blog URL:").pack()
entry_url = tk.Entry(root, width=50)
entry_url.pack()

tk.Label(root, text="Comment:").pack()
entry_comment = tk.Entry(root, width=50)
entry_comment.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
