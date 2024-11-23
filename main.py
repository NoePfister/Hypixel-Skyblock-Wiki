# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import webbrowser


class HelloWorld(FlowLauncher):

    def query(self, query):
        return [
            {
                "Title": "{}".format(('Search for: ' + query , query)[query == '']),
                "SubTitle": "Press Enter to Search.",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": [f"https://wiki.hypixel.net/index.php?search={query.strip()}"]
                }
            }
        ]

    def context_menu(self, data):
        return [
            {
                "Title": "Context Menu",
                "SubTitle": "Press Enter to Search.",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": [f"https://wiki.hypixel.net/index.php?search={data.strip()}"]
                }}
            }
        ]

    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    HelloWorld()
