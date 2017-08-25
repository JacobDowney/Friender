


from user import User
import webapp2
import jinja2
from google.appengine.api import users
from random import randint


env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

listOfHobbies = ['hobbyArt','Baseball','Basketball','Biking','Bowling','Chess',
                'Eating','Fishing','Football','Golf','GoKartRacing','Hiking',
                'MountainBiking','Photography','RacingPigeons','RockClimbing',
                'Shopping','Skateboarding','Snowboarding','Soccer','Surfing',
                'Tennis','VideoGames','Volleyball','Yoga']


listOfProfileImages = ["http://www.dailyfreepsd.com/wp-content/uploads/2013/07/Free-Minimal-Phone-Background-PSD-120x120.png",
                       "http://hotcelebwallpaperz.com/wp-content/uploads/2017/05/29/Pink-Macro-Background-120x120.jpg",
                       "https://sftextures.com/wp-content/uploads/2016/10/yellow-fluffy-dandelion-flower-transparent-background-bright-weed-plant-120x120.png",
                       "http://www.myfreetextures.com/wp-content/uploads/2014/11/blue-abstract-background-texture-120x120.jpg",
                       "http://nbtravelguide.com/wp-content/uploads/2014/05/nature-120x120.jpg",
                       "http://www.behtarlife.com/wp-content/uploads/2016/10/new-seven-wonders-of-nature-in-hindi-kmodo-120x120.jpg",
                       "http://hotcelebwallpaperz.com/wp-content/uploads/2017/03/Awesome-Nature-Wallpaper-36-120x120.jpg",
                       "https://us.v-cdn.net/5020684/uploads/userpics/103/n0MMDUNMWILW8.jpg",
                       "http://debrarubyphotography.com/wp-content/uploads/2016/08/IPhone-Pictures-11.12-1.13-259-120x120.jpg",
                       "https://usercontent1.hubstatic.com/11160346_f120.jpg"]



class MainHandler(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()

        if user:
            user_query = User.query(User.user_id == user.user_id())
            user_users = user_query.fetch()

            if user_users == []:
                greeting = ('''Welcome, %s! <br><br><br> <a href="createprofile.html" class="button">Create Profile</a>
                                <a href="%s" class="button">Log Out</a>''' %
                    (user.nickname(), users.create_logout_url('/')))
            else:
                greeting = ('''Welcome, %s! <br><br><br><a href="home.html" class="button">Go To Home</a>
                                <a href="%s" class="button">Log Out</a>''' %
                    (user.nickname(), users.create_logout_url('/')))

        else:
            greeting = ('<a href="%s" class="button">Sign in or register</a>' %
                (users.create_login_url('/')))

        template_variables = {
            'theGreeting':greeting
        }

        self.response.write('<html><body><br></body></html>')
        main_template = env.get_template("index.html")
        self.response.write(main_template.render(template_variables))



class CreateUserHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        main_template = env.get_template("createprofile.html")
        self.response.write(main_template.render())
    def post(self):

        dictOfInputHobbies = {
            'Art':self.request.get('hobbyArt'),
            'Baseball':self.request.get('hobbyBaseball'),
            'Basketball':self.request.get('hobbyBasketball'),
            'Biking':self.request.get('hobbyBiking'),
            'Bowling':self.request.get('hobbyBowling'),
            'Chess':self.request.get('hobbyChess'),
            'Eating':self.request.get('hobbyEating'),
            'Fishing':self.request.get('hobbyFishing'),
            'Football':self.request.get('hobbyFootball'),
            'Golf':self.request.get('hobbyGolf'),
            'GoKartRacing':self.request.get('hobbyGoKartRacing'),
            'Hiking':self.request.get('hobbyHiking'),
            'MountainBiking':self.request.get('hobbyMountainBiking'),
            'Photography':self.request.get('hobbyPhotography'),
            'RacingPigeons':self.request.get('hobbyRacingPigeons'),
            'RockClimbing':self.request.get('hobbyRockClimbing'),
            'Shopping':self.request.get('hobbyShopping'),
            'Skateboarding':self.request.get('hobbySkateboarding'),
            'Snowboarding':self.request.get('hobbySnowboarding'),
            'Soccer':self.request.get('hobbySoccer'),
            'Surfing':self.request.get('hobbySurfing'),
            'Tennis':self.request.get('hobbyTennis'),
            'VideoGames':self.request.get('hobbyVideoGames'),
            'Volleyball':self.request.get('hobbyVolleyball'),
            'Yoga':self.request.get('hobbyYoga')
        }

        theListOfHobbies = []

        for k, v in dictOfInputHobbies.iteritems():
            if v != "":
                theListOfHobbies.append(v)

        theImg = listOfProfileImages[randint(0, (len(listOfProfileImages)) - 1)]


        user = users.get_current_user()
        result_template = env.get_template("myprofile.html")
        template_variables = {
            'first_name':self.request.get('first_name'),
            'last_name':self.request.get('last_name'),
            'about_you':self.request.get('about_you'),
            'favorite_hobby':self.request.get('favorite_hobby').lower().capitalize(),
            'instagram_account':self.request.get('instagram_account'),
            'facebook_account':self.request.get('facebook_account'),
            'snapchat_account':self.request.get('snapchat_account'),
            'phone_number':self.request.get('phone_number'),
            'hobbies':theListOfHobbies,
            'profileImage':theImg
        }

        theUser = User(
            user_id = user.user_id(),
            first_name = template_variables['first_name'],
            last_name = template_variables['last_name'],
            about_you = template_variables['about_you'],
            favorite_hobby = template_variables['favorite_hobby'],
            instagram_account = template_variables['instagram_account'],
            facebook_account = template_variables['facebook_account'],
            snapchat_account = template_variables['snapchat_account'],
            phone_number = template_variables['phone_number'],
            hobbies = template_variables['hobbies']).put()

        self.response.write(result_template.render(template_variables))


class LogInHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        main_template = env.get_template("login.html")
        self.response.write(main_template.render())

class HomeHandler(webapp2.RequestHandler):
    def get(self):


        user = users.get_current_user()
        main_template = env.get_template("home.html")

        myUser = User.query(User.user_id == user.user_id()).get()

        userQuery = User.query(User.user_id != user.user_id())
        allUsers = userQuery.fetch()

        listOfUsersWithAnyMathcingHobbies = []

        myBool = False

        for theCurrentUser in allUsers:
            for theCurrentHobby in theCurrentUser.hobbies:
                if myBool == True:
                    myBool = False
                    break
                for myCurrentHobby in myUser.hobbies:
                    if theCurrentHobby == myCurrentHobby:
                        myBool = True
                        listOfUsersWithAnyMathcingHobbies.append(theCurrentUser)
                        break

        theImgs = []

        for i in range(0, len(listOfUsersWithAnyMathcingHobbies)):
            theImgs.append(listOfProfileImages[randint(0, (len(listOfProfileImages)) - 1)])


        greeting = ('<a href="%s" class="button">Log Out</a>' % (users.create_logout_url('/')))
        template_variables = {
            'theGreeting': greeting,
            'listOfUsers':listOfUsersWithAnyMathcingHobbies,
            'profileImages':theImgs
        }


        self.response.write(main_template.render(template_variables))


class SearchHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        main_template = env.get_template("search.html")

        greeting = ('<a href="%s">Log Out</a>' % (users.create_logout_url('/')))
        template_variables = {
            'theGreeting': greeting
        }

        self.response.write(main_template.render(template_variables))
    def post(self):
        user = users.get_current_user()
        result_template = env.get_template("aftersearch.html")

        userQuery = User.query(User.user_id != user.user_id())
        allUsers = userQuery.fetch()

        theSearch = self.request.get('yourSearch').lower().capitalize()

        listOfUsersWithMathcingHobbies = []

        for theCurrentUser in allUsers:
            for theCurrentHobby in theCurrentUser.hobbies:
                if (theSearch == theCurrentHobby):
                    listOfUsersWithMathcingHobbies.append(theCurrentUser)

        theImgs = []

        for i in range(0, len(listOfUsersWithMathcingHobbies)):
            theImgs.append(listOfProfileImages[randint(0, (len(listOfProfileImages)) - 1)])

        greeting = ('<a href="%s" class="button">Log Out</a>' % (users.create_logout_url('/')))

        template_variables = {
            'theUsers': listOfUsersWithMathcingHobbies,
            'theGreeting': greeting,
            'profileImages':theImgs
        }


        self.response.write(result_template.render(template_variables))



class MyProfileHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        user_query = User.query(User.user_id == user.user_id())
        current_user_data = user_query.get()

        greeting = ('<a href="%s" class="button">Log Out</a>' % (users.create_logout_url('/')))


        theImg = listOfProfileImages[randint(0, (len(listOfProfileImages)) - 1)]

        template_variables = {
            'first_name': current_user_data.first_name,
            'last_name': current_user_data.last_name,
            'about_you': current_user_data.about_you,
            'favorite_hobby': current_user_data.favorite_hobby,
            'instagram_account': current_user_data.instagram_account,
            'facebook_account': current_user_data.facebook_account,
            'snapchat_account': current_user_data.snapchat_account,
            'phone_number': current_user_data.phone_number,
            'hobbies':current_user_data.hobbies,
            'theGreeting':greeting,
            'profileImage': theImg
        }
        main_template = env.get_template("myprofile.html")
        self.response.write(main_template.render(template_variables))


class EditProfileHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        user_query = User.query(User.user_id == user.user_id())
        current_user_data = user_query.get()
        greeting = ('<a href="%s" class="button">Log Out</a>' % (users.create_logout_url('/')))
        template_variables = {
            'user_obj': current_user_data,
            'greeting': greeting
            }
        main_template = env.get_template("editprofile.html")
        self.response.write(main_template.render(template_variables))
    def post(self):
        dictOfInputHobbies = {
            'Art':self.request.get('hobbyArt'),
            'Baseball':self.request.get('hobbyBaseball'),
            'Basketball':self.request.get('hobbyBasketball'),
            'Biking':self.request.get('hobbyBiking'),
            'Bowling':self.request.get('hobbyBowling'),
            'Chess':self.request.get('hobbyChess'),
            'Eating':self.request.get('hobbyEating'),
            'Fishing':self.request.get('hobbyFishing'),
            'Football':self.request.get('hobbyFootball'),
            'Golf':self.request.get('hobbyGolf'),
            'GoKartRacing':self.request.get('hobbyGoKartRacing'),
            'Hiking':self.request.get('hobbyHiking'),
            'MountainBiking':self.request.get('hobbyMountainBiking'),
            'Photography':self.request.get('hobbyPhotography'),
            'RacingPigeons':self.request.get('hobbyRacingPigeons'),
            'RockClimbing':self.request.get('hobbyRockClimbing'),
            'Shopping':self.request.get('hobbyShopping'),
            'Skateboarding':self.request.get('hobbySkateboarding'),
            'Snowboarding':self.request.get('hobbySnowboarding'),
            'Soccer':self.request.get('hobbySoccer'),
            'Surfing':self.request.get('hobbySurfing'),
            'Tennis':self.request.get('hobbyTennis'),
            'VideoGames':self.request.get('hobbyVideoGames'),
            'Volleyball':self.request.get('hobbyVolleyball'),
            'Yoga':self.request.get('hobbyYoga'),
        }

        theListOfHobbies = []

        for k, v in dictOfInputHobbies.iteritems():
            if v != "":
                theListOfHobbies.append(v)

        theImg = listOfProfileImages[randint(0, (len(listOfProfileImages)) - 1)]

        greeting = ('<a href="%s" class="button">Log Out</a>' % (users.create_logout_url('/')))


        user = users.get_current_user()
        user_query = User.query(User.user_id == user.user_id())
        current_user_data = user_query.get()
        result_template = env.get_template("myprofile.html")
        template_variables = {
            'user_obj': current_user_data,
            'first_name':self.request.get('first_name'),
            'last_name':self.request.get('last_name'),
            'about_you':self.request.get('about_you'),
            'favorite_hobby':self.request.get('favorite_hobby').lower().capitalize(),
            'instagram_account':self.request.get('instagram_account'),
            'facebook_account':self.request.get('facebook_account'),
            'snapchat_account':self.request.get('snapchat_account'),
            'phone_number':self.request.get('phone_number'),
            'hobbies':theListOfHobbies,
            'theGreeting':greeting,
            'profileImage':theImg
        }

        current_user_data.user_id = user.user_id()
        current_user_data.first_name = template_variables['first_name']
        current_user_data.last_name = template_variables['last_name']
        current_user_data.about_you = template_variables['about_you']
        current_user_data.favorite_hobby = template_variables['favorite_hobby']
        current_user_data.instagram_account = template_variables['instagram_account']
        current_user_data.facebook_account = template_variables['facebook_account']
        current_user_data.snapchat_account = template_variables['snapchat_account']
        current_user_data.phone_number = template_variables['phone_number']
        current_user_data.hobbies = template_variables['hobbies']
        current_user_data.put()

        self.response.write(result_template.render(template_variables))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login.html', LogInHandler),
    ('/createprofile.html', CreateUserHandler),
    ('/home.html', HomeHandler),
    ('/search.html', SearchHandler),
    ('/myprofile.html', MyProfileHandler),
    ('/editprofile.html', EditProfileHandler)
], debug=True)
