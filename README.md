# floof bot
A GroupMe chatbot that sends pictures of cute, fluffy dogs and cats! Uses the [dog.ceo API](https://dog.ceo/dog-api/) for getting pictures of dogs and [thecatapi.com](http://thecatapi.com) for pictures of cats. Supports a lot of different dog breeds and sub-breeds ([list](https://dog.ceo/dog-api/breeds-list)).

### Use the floof bot in your own chat
There are a few simple steps involved here.
1. Deploy the app to Heroku using this button. Give it a memorable name; we will need it later.

    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy&env[GROUPME_BOT_ID]=default)
2. Create a bot user at the [GroupMe dev site](https://dev.groupme.com/bots). Assign it to the chat you want to add it, give it a name and an avatar, and for the callback URL, use **https://`<name>`.herokuapp.com** where `<name>` corresponds to the name you used in step #1.
3. Now copy the "bot ID" field on the GroupMe dev site.
4. Go to your app dashboard on Heroku and in the settings tab, change the configuration variable `GROUPME_BOT_ID` from default to the value you copied in step #3.
5. We are done now! Trigger the bot in your chat by saying "dog" or "cat" or "floof" or "cloud" or any of the breeds of dogs.
