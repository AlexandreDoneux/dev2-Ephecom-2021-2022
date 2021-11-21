class FindWay:
    def __init__(self, origin, destination):
        self._origin = origin
        self._destination = destination

    def find(self, origin, destination):

        #Simple Program to help you get started with Google's APIs

        import urllib.request, json
        #Google MapsDdirections API endpoint
        endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
        api_key = 'AIzaSyCynvNoSNRz6HQLkptj-n_cLr8rn7CJPxk'
        #Asks the user to input Where they are and where they want to go.
        self.origin = input('Where are you?: ').replace(' ','+')
        self.destination = input('Where do you want to go?: ').replace(' ','+')
        #Building the URL for the request
        nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
        request = endpoint + nav_request
        #Sends the request and reads the response.
        response = urllib.request.urlopen(request).read()
        #Loads response as JSON
        directions = json.loads(response)
        print(directions)


# Géolocaliser grâce à son adresse ip
#tracert + l'ip

#Adresse actuelle grâce à l'ip
# cmd ipconfig




