import service
import re
import logging

#ref2 branch
__VERSION__ = "2.2.2.2.2.2"


def ref2_branch():
    print(f'new ref2 branch')


def main():
    pattern = re.compile(r'\d\w\s\s\s\s\s\s')
    print_header()
    service.download_info()
    show_titles()


def print_me():
    print(f'print me')
    print(f'print me')
    print(f'print me')
    print(f'print me')


def print_header():
    print("------------------------------------------")
    print(f"  TALK PYTHON PODCAST DOWNLOADER v{__VERSION__}")
    print("------------------------------------------")


def show_titles():
    start = service.get_min_episode_id()
    end = service.get_max_episode_id()

    for episode_id in range(start, end + 1):
        show_episode_details(episode_id)


def show_episode_details(episode_id: int):
    episode = service.get_details(episode_id)
    print(f'{episode.id}. -> {episode.title}')


if __name__ == '__main__':
    main()
