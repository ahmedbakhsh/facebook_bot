from selenium import webdriver 
import time

final_comments = []
with open('comment.txt') as comment:
    comments = comment.readline()
    striped_comment = comments.replace(' ',"")
    for comment in striped_comment:
        final_comments.append(comment)
     
def auto_comment(final_comments):
    browser = webdriver.Chrome()
    browser.get("https://mbasic.facebook.com")

    email = browser.find_element_by_css_selector("input[name='email']")
    email.send_keys("9810831044")
    time.sleep(1)

    password = browser.find_element_by_css_selector("input[name='pass']")
    password.send_keys("loveyouarju")
    button = browser.find_element_by_css_selector("input[type='submit']")
    button.click()
    time.sleep(2)

    browser.get("https://mbasic.facebook.com/story.php?story_fbid=2556937301227415&id=100007335102460&refid=17&_ft_=mf_story_key.2556937301227415%3Atop_level_post_id.2556937301227415%3Atl_objid.2556937301227415%3Acontent_owner_id_new.100007335102460%3Aoriginal_content_id.4260380450642462%3Aoriginal_content_owner_id.172819872731894%3Athrowback_story_fbid.2556937301227415%3Astory_location.4%3Astory_attachment_style.share%3Athid.100007335102460%3A306061129499414%3A2%3A0%3A1588316399%3A-5876329860260598811&__tn__=%2AW-R")

    for i in len(final_comments):
        cb = browser.find_element_by_css_selector("textarea[name='comment_text']")
        cb.send_keys(final_comments[int(i)])

        button = browser.find_element_by_css_selector("input[type='submit']")
        button.click()

        time.sleep(2)
        print(f'{i} comment is done !!')

if __name__ == "__main__":
    pass

