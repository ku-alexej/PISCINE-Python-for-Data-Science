import os
import time


def ft_tqdm(lst: range) -> None:
    '''
    A function that mimics the behavior of tqdm by displaying a progress bar in the terminal.
    '''
    total = len(lst)
    terminal_width = os.get_terminal_size().columns

    start_time = time.time()

    fixed_size = len(f"100%| | {total}/{total} [00:00<00:00, 999.99it/s]")
    bar_size = max(1, terminal_width - fixed_size)

    for i, elem in enumerate(lst, 1):
        elapsed = time.time() - start_time
        rest_time = (elapsed / i) * (total - i) if i > 0 else 0

        if elapsed > 0:
            speed = i / elapsed
        else:
            speed = 0

        percent = i / total
        filled = int(percent * bar_size)

        if speed >= 100000:
            speed_str = f"{speed/1000:.1f}kit/s"
        else:
            speed_str = f"{speed:.2f}it/s"

        line = (
            f"{percent * 100:3.0f}%|"
            f"{"█" * bar_size if i == total else "█" * filled + " " * (bar_size - filled)}| "
            f"{i}/{total} "
            f"[{int(elapsed // 60):02d}:{int(elapsed % 60):02d}<"
            f"{int(rest_time // 60):02d}:{int(rest_time % 60):02d}, {speed_str}]"
        )

        print("\r" + line.ljust(terminal_width), end="", flush=True)

        yield elem

    print()
