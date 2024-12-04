import os
from datetime import datetime
from plyer import notification
import webbrowser
from datetime import datetime


blogs = [
    "https://netflixtechblog.com/",
    "http://eng.uber.com/",
    "https://blog.cloudflare.com/",
    "https://engineering.fb.com/",
    "https://research.google/blog/",
    "https://cloud.google.com/blog/",
    "https://blogs.nvidia.com/",
    "https://www.linkedin.com/blog/engineering",
    "https://engineering.linkedin.com/blog",
    "https://aws.amazon.com/blogs/architecture/",
    "https://stripe.com/blog/engineering",
    "https://discord.com/category/engineering",
    "https://slack.engineering/",
    "https://blog.asana.com/category/eng/",
    "https://developer.atlassian.com/blog/",
    "https://auth0.com/blog/",
    "https://aws.amazon.com/blogs/",
    "https://blog.x.com/engineering/en_us",
    "https://softwaremill.com/",
    "https://blog.booking.com/",
    "https://www.canva.dev/blog/engineering/",
    "https://blog.cloudera.com/",
    "https://engineering.atspotify.com/",
    "https://openai.com/news/research/",
    "https://www.cockroachlabs.com/blog/",
    "https://engineering.coinbase.com/",
    "https://www.confluent.io/blog",
    "https://engineering.creditkarma.com/",
    "https://databricks.com/blog",
    "https://blog.docker.com/",
    "https://dropbox.tech/",
    "https://doordash.engineering/blog/",
    "https://blogs.dropbox.com/tech/",
    "https://innovation.ebayinc.com/tech/",
    "https://www.elastic.co/blog",
    "https://www.eventbrite.com/engineering/",
    "https://medium.com/expedia-group-tech",
    "https://github.blog/engineering/",
    "http://engineering.grab.com/",
    "https://grafana.com/blog/",
    "https://engineering.groupon.com/",
    "http://engineering.gusto.com/",
    "https://www.edgeimpulse.com/blog/",
    "https://blog.heroku.com/engineering",
    "http://product.hubspot.com/blog/topic/engineering",
    "http://engineering.indeedblog.com/blog/",
    "https://tech.instacart.com/",
    "https://blog.hotstar.com/",
    "https://bytes.swiggy.com/",
    "https://instagram-engineering.com/",
    "https://software.intel.com/en-us/blogs/",
    "https://blogs.janestreet.com/category/ocaml/",
    "http://engineering.khanacademy.org/",
    "https://engineering.linecorp.com/en/blog",
    "https://eng.lyft.com/",
    "https://engineering.mixpanel.com/",
    "https://engblog.nextdoor.com/",
    "https://developer.okta.com/blog/",
    "https://www.paypal-engineering.com/",
    "https://medium.com/Pinterest_Engineering",
    "https://blog.postman.com/",
    "https://www.etsy.com/codeascraft",
    "https://www.pubnub.com/blog/",
    "https://engineering.quora.com/",
    "http://blog.rapidapi.com/",
    "https://www.reddit.com/r/RedditEng/",
    "https://developers.redhat.com/blog/",
    "https://engineering.riotgames.com/",
    "https://eng.snap.com/blog",
    "https://www.databricks.com/blog/category/engineering",
    "https://shopify.engineering/",
    "https://corner.squareup.com/",
    "https://engineering.squarespace.com/",
    "https://stackoverflow.blog/engineering/",
    "http://multithreaded.stitchfix.com/blog/",
    "https://engineering.surveymonkey.com/",
    "https://www.thoughtworks.com/insights",
    "https://www.thumbtack.com/engineering/",
    "https://blog.timescale.com/",
    "https://tech.gotinder.com/",
    "https://www.toptal.com/blog/",
    "https://www.twilio.com/blog/",
    "https://blog.twitter.com/engineering",
    "https://blog.twitch.tv/en/tags/engineering/",
    "http://engineering.wayfair.com/",
    "https://engineeringblog.yelp.com/",
    "https://medium.com/airbnb-engineering",
    "https://zapier.com/engineering/",
    "https://medium.com/zendesk-engineering",
    "https://www.zillow.com/engineering/",
    "https://engineering.zomato.com/",
    "https://developers.zoom.us/blog/",
    "https://www.zynga.com/blogs/engineering"

]

def send_reminder():
    current_day_of_year =  datetime.now().timetuple().tm_yday
    blog_index = current_day_of_year % len(blogs)
    blog_url = blogs[blog_index]

    notification.notify(
        title="Blog Reminder",
        message=f"Reminder: Read the blog: {blog_url}",
        timeout=100  
    )
    
    webbrowser.open(blog_url)
    os._exit(0)
    
send_reminder()