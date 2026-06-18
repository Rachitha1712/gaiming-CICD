def game_performance(fps):

    if fps < 30:
        return "high PERFORMANCE"

    elif fps < 60:
        return "MODERATE PERFORMANCE"

    else:
        return "SMOOTH GAMEPLAY"


if __name__ == "__main__":

    fps = int(input("Enter FPS: "))

    print(game_performance(fps))