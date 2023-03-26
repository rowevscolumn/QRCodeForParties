import qrcode
import json

class CreateQRCode:
    """
    Description of CreateQRCode

    Attributes:
        qrjson (str): Location of the JSON file with the Wifi information
        outImage (str): File name of the png file that will save the QR code
        qrstat (dict): Dictionary of all the wifi stats ("available security" is a list of all available securities for reference)
        qrlink (str): The output link. Will be fed into the QRcode library to make image
        wifi_qrcode (qrcode): QRCode library with all the information

    Args:
        qrjson (str='WifiPassword.json'): Location of the JSON file with the Wifi information
        outImage (str="wifi_qrcode.png"): File name of the png file that will save the QR code

    """
    def __init__(self, qrjson: str = 'WifiPassword.json', outImage:str = "wifi_qrcode.png") -> None:
        self.qrjson:str = qrjson
        self.outImage:str = outImage
        self.qrstat:dict = self.__loadJsonFile()
        self.qrlink:str = self.__createLink()
        self.wifi_qrcode:qrcode = self.__makeImage()
        pass

    def __str__(self) -> str:
        return self.qrlink

    def __loadJsonFile(self) -> dict:
        """
        Loads the JSON file, adds it to a dictionary.

        Returns:
            dict: Dictionary of settings
        """
        with open(self.qrjson) as json_file:
            data = json.load(json_file)
        return data
    
    def __createLink(self) -> str:
        """
        Creates the Wifi link from the JSON values. Make sure they are correct.

        Returns:
            str: The wifi link in string format
        """
        link = f"WIFI:T:{self.qrstat['wifi_name']};S:{self.qrstat['wifi_password']};P:{self.qrstat['security_key']};;"
        return link
    
    def __makeImage(self) -> qrcode:
        """
        Makes the image into the QRCode library

        Returns:
            qrcode

        """
        return qrcode.make(self.qrlink)

    
    def saveimage(self, newpath: str = None) -> bool:
        """
        Saves the image to a PNG file. Perfect for printing the image or add to a Photoshop

        Args:
            newpath (str=None): If the file name wants to be changed

        Returns:
            bool
        """
        if newpath:
            self.outImage = newpath
        self.wifi_qrcode.save(self.outImage) # This will save the image as a png
        return True
    
    def returnforDisplay(self) -> qrcode:
        """
        Returns the QR code for the purposes of displaying onto Jupyter Notebook

        Returns:
            qrcode

        """
        return self.wifi_qrcode
    
    pass # END class CreateQRCode
