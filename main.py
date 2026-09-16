import os
import sys
import yt_dlp
from colorama import Fore, Style, init

# Colorama-nı avtomatik sıfırlama rejimi ilə başladırıq
init(autoreset=True)

TRANSLATIONS = {
    "en": {
        "welcome": f"\n{Fore.CYAN}=== INSTAGRAM STORY & REEL DOWNLOADER ===",
        "created_by": f"{Fore.YELLOW}Created by: RuslanSharifov (https://github.com/RuslanSharifov)",
        "input_link": f"{Fore.WHITE}Enter Instagram Story/Reel link: ",
        "checking": f"{Fore.BLUE}[+] Fetching video data...",
        "success": f"\n{Fore.GREEN}[✓] Video successfully downloaded to 'downloads' folder!",
        "error": f"{Fore.RED}[-] Download failed. Please ensure the link is valid and public.",
        "no_cookies_warning": (
            f"\n{Fore.YELLOW}[!] WARNING: 'cookies.txt' file was not found in the project folder!\n"
            f"{Fore.WHITE}    Instagram Stories require authentication to be downloaded.\n"
            f"    How to fix this:\n"
            f"    1. Install 'Get cookies.txt LOCALLY' extension in your browser.\n"
            f"    2. Log in to Instagram and export your cookies.\n"
            f"    3. Place the downloaded 'cookies.txt' file in this folder:\n"
            f"{Fore.CYAN}       {os.getcwd()}\n"
        ),
        "no_link": f"{Fore.RED}[-] No link provided.",
        "press_enter": f"\n{Fore.MAGENTA}Press Enter to exit...",
        "select_lang": f"{Fore.WHITE}Select choice (1-3) [Default: EN]: "
    },
    "ru": {
        "welcome": f"\n{Fore.CYAN}=== INSTAGRAM STORY & REEL DOWNLOADER ===",
        "created_by": f"{Fore.YELLOW}Автор: RuslanSharifov (https://github.com/RuslanSharifov)",
        "input_link": f"{Fore.WHITE}Введите ссылку на Instagram Story/Reel: ",
        "checking": f"{Fore.BLUE}[+] Получение данных видео...",
        "success": f"\n{Fore.GREEN}[✓] Видео успешно загружено в папку 'downloads'!",
        "error": f"{Fore.RED}[-] Ошибка скачивания. Убедитесь, что ссылка верна.",
        "no_cookies_warning": (
            f"\n{Fore.YELLOW}[!] ВНИМАНИЕ: Файл 'cookies.txt' не найден!\n"
            f"{Fore.WHITE}    Для скачивания Stories необходима авторизация.\n"
            f"    Инструкция:\n"
            f"    1. Установите расширение 'Get cookies.txt LOCALLY' в браузер.\n"
            f"    2. Войдите в Instagram и экспортируйте cookies.\n"
            f"    3. Поместите файл 'cookies.txt' в эту папку:\n"
            f"{Fore.CYAN}       {os.getcwd()}\n"
        ),
        "no_link": f"{Fore.RED}[-] Ссылка не введена.",
        "press_enter": f"\n{Fore.MAGENTA}Нажмите Enter для выхода...",
        "select_lang": f"{Fore.WHITE}Выберите язык (1-3) [По умолчанию: EN]: "
    },
    "zh": {
        "welcome": f"\n{Fore.CYAN}=== INSTAGRAM STORY & REEL DOWNLOADER ===",
        "created_by": f"{Fore.YELLOW}作者: RuslanSharifov (https://github.com/RuslanSharifov)",
        "input_link": f"{Fore.WHITE}请输入 Instagram Story/Reel 链接: ",
        "checking": f"{Fore.BLUE}[+] 正在获取视频数据...",
        "success": f"\n{Fore.GREEN}[✓] 视频已成功下载到 'downloads' 文件夹！",
        "error": f"{Fore.RED}[-] 下载失败。请确保链接有效。",
        "no_cookies_warning": (
            f"\n{Fore.YELLOW}[!] 警告: 未找到 'cookies.txt' 文件！\n"
            f"{Fore.WHITE}    下载 Story 需要登录验证。\n"
            f"    解决方法:\n"
            f"    1. 在浏览器中安装 'Get cookies.txt LOCALLY' 插件。\n"
            f"    2. 登录 Instagram 并导出 cookies。\n"
            f"    3. 将 'cookies.txt' 文件放入此文件夹:\n"
            f"{Fore.CYAN}       {os.getcwd()}\n"
        ),
        "no_link": f"{Fore.RED}[-] 未提供链接。",
        "press_enter": f"\n{Fore.MAGENTA}按 Enter 键退出...",
        "select_lang": f"{Fore.WHITE}选择语言 (1-3) [默认: EN]: "
    }
}

def choose_language():
    print(f"{Fore.GREEN}============================================")
    print(f"{Fore.WHITE} 1. English (EN) [Default]")
    print(f"{Fore.WHITE} 2. Русский (RU)")
    print(f"{Fore.WHITE} 3. 中文 (ZH)")
    print(f"{Fore.GREEN}============================================")
    choice = input(TRANSLATIONS["en"]["select_lang"]).strip()
    
    lang_map = {"1": "en", "2": "ru", "3": "zh"}
    selected_lang = lang_map.get(choice, "en")
    return TRANSLATIONS[selected_lang]

def download_story(url, t):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': 'downloads/%(uploader)s_%(id)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
    }

    if os.path.exists('cookies.txt'):
        ydl_opts['cookiefile'] = 'cookies.txt'
    else:
        print(t["no_cookies_warning"])

    try:
        print(t["checking"])
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if not os.path.exists('downloads'):
                os.makedirs('downloads')
            ydl.download([url])
            print(t["success"])
    except Exception:
        print(t["error"])


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    t = choose_language()
    
    print(t["welcome"])
    print(t["created_by"])
    print(f"{Fore.CYAN}" + "=" * 44)

    if len(sys.argv) > 1:
        link = sys.argv[1]
    else:
        link = input(t["input_link"]).strip()

    if link:
        download_story(link, t)
    else:
        print(t["no_link"])

    input(t["press_enter"])

if __name__ == "__main__":
    main()