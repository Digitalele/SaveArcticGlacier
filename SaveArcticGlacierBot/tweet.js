console.log('The reply bot is starting');

var Twit = require('twit');

var config = require('./config');
var T = new Twit(config);

// Setting up a user stream
var stream = T.stream('user');

stream.on('tweet', tweetEvent);

// Every time someone tweet me
function tweetEvent(eventMsg) {
  var replyto = eventMsg.in_reply_to_screen_name;
  var text = eventMsg.text;
  var from = eventMsg.user.screen_name;

  console.log(replyto + ' ' + from + ' ' + text);

if (replyto === 'Save_Arctic_Ice'){
  var newtweet = '@' + from + ' Thanks for having tweeted #SaveTheArcticGlacier!'
  tweetIt(newtweet);
  }
}

function tweetIt(txt) {

    var tweet = {
      status: txt
    }

    T.post('statuses/update', tweet, tweeted);

    function tweeted(err, data, response) {
      if (err) {
        console.log("Something went wwrong!");
      } else {
        console.log("It worked!");
      }
    }
}