import os
import time


def ft_tqdm(lst: range) -> None:
    '''
    A function that mimics the behavior of tqdm by
    displaying a progress bar in the terminal.
    '''
    total = len(lst)
    terminal_width = os.get_terminal_size().columns

    start_time = time.time()

    # calculate size
    fixed_s = len(f"100%| | {total}/{total} [00:00<00:00, 999.99it/s]")
    bar_s = max(1, terminal_width - fixed_s)

    for i, elem in enumerate(lst, 1):

        # calculate elapsed time, remaining time
        ela_t = time.time() - start_time
        rem_t = (ela_t / i) * (total - i) if i > 0 else 0

        if ela_t > 0:
            speed = i / ela_t
        else:
            speed = 0

        percent = i / total
        filled = int(percent * bar_s)

        if speed >= 100000:
            speed_str = f"{speed/1000:.1f}kit/s"
        else:
            speed_str = f"{speed:.2f}it/s"

        if i == total:
            bar_line = "█" * bar_s
        else:
            bar_line = "█" * filled + " " * (bar_s - filled)

        line = (
            f"{percent * 100:3.0f}%|"
            f"{bar_line}| "
            f"{i}/{total} "
            f"[{int(ela_t // 60):02d}:{int(ela_t % 60):02d}<"
            f"{int(rem_t // 60):02d}:{int(rem_t % 60):02d}, {speed_str}]"
        )

        print("\r" + line.ljust(terminal_width), end="", flush=True)

        yield elem

    print()
