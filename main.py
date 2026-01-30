import os
import re
from InquirerPy import inquirer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from dotenv import load_dotenv


load_dotenv()


def clean_query(text):
    text = re.sub(r"[^\w\s]", "", text)  # remove emojis
    return text.strip()


def open_youtube_and_play(search_query):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.youtube.com")

        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.ENTER)

        first_video = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '(//ytd-video-renderer//a[@id="video-title"])[1]')
            )
        )

        print("▶ Playing:", first_video.text)
        first_video.click()

        sleep(60)

    except Exception as e:
        print("❌ Automation error:", e)


def choose_category():
    return inquirer.select(
        message="🎯 Select Category:",
        choices=[
            "F1", "ANIME", "MOVIES", "WEB-SERIES",
            "GAMING-VIDEOS", "ANIMATIONS",
            "CARTOONS", "STUDY-STUFF"
        ]
    ).execute()


def f1_flow():
    years = list(range(2000, 2026))
    gps = [
        "ABU DHABI GRAND PRIX 🏎️", "SAO PAULO GRAND PRIX 🏎️",
        "MONACO GRAND PRIX 🏎️", "BRITISH GRAND PRIX 🏎️",
        "LAS VEGAS GRAND PRIX 🏎️", "MIAMI GRAND PRIX 🏎️",
        "AUSTRALIAN GRAND PRIX 🏎️", "ITALIAN GRAND PRIX 🏎️",
        "BELGIAN GRAND PRIX 🏎️", "SINGAPORE GRAND PRIX 🏎️",
        "CHINESE GRAND PRIX 🏎️", "SAUDI ARABIAN GRAND PRIX 🏎️",
        "EMILIA GRAND PRIX 🏎️", "DUTCH GRAND PRIX 🏎️",
        "HUNGARIAN GRAND PRIX 🏎️", "BAHRAIN GRAND PRIX 🏎️",
        "AZERBAIJAN GRAND PRIX 🏎️", "UNITED STATES GRAND PRIX 🏎️",
        "QATAR GRAND PRIX 🏎️"
    ]
    stages = ["SPRINT QUALIFYING", "SPRINT", "QUALIFYING", "RACE"]

    year = inquirer.select("📅 Choose Year:", years).execute()
    gp = inquirer.select("🏁 Choose Grand Prix:", gps).execute()
    stage = inquirer.select("🚦 Choose Stage:", stages).execute()

    return f"F1 {year} {gp} {stage}"

def anime_flow():
    anime_titles = [
        "DRAGON BALL", "NARUTO", "ONE PIECE","BLEACH",
        "DEMON SLAYER", "JUJUTSU KAISEN", "SOLO LEVELING" , "ATTACK ON TITAN", 
        "MY HERO ACADEMIA" ,"CHAINSAW MAN", "HUNTER X HUNTER" ,"ONE PUNCH MAN" ,"CLASS ROOM OF THE ELITE", "DAN - DA - DAN", "SPY X FAMILY",
        "GINTAMA","DEATH NOTE" , "BLUE LOCK" , "SAKAMOTO DAYS" , "WIND BREACKER","DR. STONE" ,"SEVEN DEADLY SINS", "TOKOYO REVENGERS","TOKOYO GOUL","RE ZERO",
        "KAGUYA SAMA","GACHIA GUTA" ,"MUSHOKO TENSAI" ,"HAJIME NO IPPO" , "HAIKYU" ,"DAYS WITH MY STEP ONII-SAN",
        "MOOB PHYCHO 100" ,"YOUR NAME" ,"FIVE CENTIMETER PER SECOND" ,"WEATHERING WITH YOU","SPRITED AWAY","BLUE BOX",
        "KAIJU NO. 8","VINLAND SAGA" ,"BLACK CLOVER" ,"FREEREN" ,"ASSASSINATION CLASSROOM",
        "I WANT TO EAT YOUR PANCREASE" ,"SLIENT VOICE","FIRE FLISE" ,"GRAND BLUE" ,"HORIMIA" ,"THE DANGERS IN MY HEART"
    ]
    sections = ["INTRO", "SEASON", "CLIPS", "TRAILER", "MOVIE"]

    anime = inquirer.select("🍥 Choose Anime:", anime_titles).execute()
    section = inquirer.select("📺 Choose Section:", sections).execute()

    return f"{anime} {section}"

def movie_flow():
    movies = [
        "IRON MAN", "CARS", "AVENGERS", "END GAME",
        "INTERSTELLAR", "YOUR NAME", "A SILENT VOICE"
    ]
    sections = ["SCENE", "CLIPS", "TRAILER"]

    movie = inquirer.select("🎬 Choose Movie:", movies).execute()
    section = inquirer.select("🎞 Choose Section:", sections).execute()

    return f"{movie} {section}"

def web_series_flow():
    series = [
        "INVINCIBLE", "THE BOYS", "STRANGER THINGS",
        "ALICE IN BORDERLAND", "GAME OF THRONE", "MONEY HEIST",
        "BREAKING BAD", "BLOOD HOUND", "WEAK HERO",
        "LOKI", "THE WITCHER", "PEAKY BLINDER"
    ]
    sections = ["SEASON", "CLIPS", "BEST SCENE"]

    s = inquirer.select("📺 Choose Series:", series).execute()
    sec = inquirer.select("🎞 Choose Section:", sections).execute()

    return f"{s} {sec}"

def gaming_flow():
    games = [
        "DELTA FORCE", "ELDEN RING", "DARK SOUL",
        "BATTLE FIELD 6", "RESIDENT EVIL", "DEMON SLAYER",
        "BLACK OPPS 6", "HORROR TYPE", "MINECRAFT",
        "GOD OF WAR", "RED DEAD REDEMPTION 2",
        "ASSASSIN'S CREED", "GTA 5", "WARZONE"
    ]
    sections = ["GAMEPLAY", "CUTSCENE", "STORY MODE"]

    g = inquirer.select("🎮 Choose Game:", games).execute()
    sec = inquirer.select("🕹 Choose Section:", sections).execute()

    return f"{g} {sec}"

def animations_flow():
    studios = [
        "UFOTABLE", "MAPPA", "FAN MADE", "PIXAR STUDIOS",
        "SONY", "GHIBLI ANIMATONS", "ILLUMINATION",
        "TOEI ANIMATIONS", "DREAM WORK", "WIT STUDIOS"
    ]
    return inquirer.select("🎨 Choose Animation:", studios).execute()

def cartoons_flow():
    cartoons = [
       "OGGY AND THE CROCKROACHES", "PAKADAM PAKADAI",
        "PENGUINS AND THE MADAGASCAR", "GON", "DOREMON",
        "SPIDER MAN", "CHOTA BHEEM", "BEN 10", "COW AND CHICKEN",
        "ADVENTURE TIME", "WE BARE BEARS", "PAW PETROLS",
        "MICKEY MOUSE", "BANDBUDH AND BUDHBAK", "MOTU PATLU",
        "LITTLE KRISHNA", "BAHUBBALI THE LOST LEGEND",
        "BUNTY BILLA AUR BABBAN", "KEYMON ACHE", "SUPER BHEEM"
    ]
    return inquirer.select("🐭 Choose Cartoon:", cartoons).execute()

def study_flow():
    topics = [
        "CODING STUFF","LEET CODE" , "WEB DEV PART", "PYTHON MODULES", "JAVA", "C++",
        "JAVASCRIPT", "HTML_CSS", "DJANGO", "FRONTEND", "BACKEND",
        "SUPABASE", "GIT", "GITHUB", "LINKDIN", 
        "SCRTCH PROJECTS", "MCP SERVERS", "OPEN ROUTER", "CODE DEX",
        "DEVFOLIO", "HAKATHOAN", "TECH STUFF", "PC STUFF",
        "ARTIFICIAL INTELLIGENCE", "LIBERARYS OF PYTHON",
        "DEEP LEARNING", "AGENTIC AI", "MODELS",
        "MACHINE LEARNING", "PROJECTS", "REPOSITORIES",
        "GO", "RUST", "RUBY", "C", "SQL", "LEET CODE STUFFS",
        "HACKER-RANK", "FAST API"
    ]
    levels = ["BEGINNER", "INTERMEDIATE", "ADVANCED"]

    t = inquirer.select("📘 Topic:", topics).execute()
    l = inquirer.select("🎓 Level:", levels).execute()

    return f"{t} {l} tutorial"


def web_search_agent():
    print("\n🤖 YouTube AI Agent Started\n")

    category = choose_category()

    if category == "F1":
        query = f1_flow()
    elif category == "ANIME":
        query = anime_flow()
    elif category == "MOVIES":
        query = movie_flow()
    elif category == "WEB-SERIES":
        query = web_series_flow()
    elif category == "GAMING-VIDEOS":
        query = gaming_flow()
    elif category == "ANIMATIONS":
        query = animations_flow()
    elif category == "CARTOONS":
        query = cartoons_flow()
    elif category == "STUDY-STUFF":
        query = study_flow()
    else:
        return

    final_query = clean_query(query)
    print("\n🔎 Searching:", final_query)
    open_youtube_and_play(final_query)


if __name__ == "__main__":
    web_search_agent()
