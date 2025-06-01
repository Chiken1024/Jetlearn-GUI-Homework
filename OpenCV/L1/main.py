import cv2 as cv


class Main:
  def __init__(self, filepath: str) -> None:
    self.FILEPATH: str = filepath

    self.rgb: str[3] = ["Red", "Green", "Blue"]
  
  def save_image(self, path: str, rgb: int) -> None:
    image: cv.Mat = cv.imread(f"{self.FILEPATH}{path}.png", 1)
    
    cv.imshow("Image preview", cv.split(image)[rgb])

    cv.imwrite(f"{self.FILEPATH}{path} ({self.rgb[rgb]}).png", image)
    print("Succesfully saved image!")
    
    cv.waitKey(delay=1000)
    cv.destroyAllWindows()


if __name__ == "__main__":
  Main("L1/").save_image("pikachu", 0)