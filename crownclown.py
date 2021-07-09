import praw
import os
import random
import time
from time import sleep

reddit = praw.Reddit(
  client_id = os.getenv('client_id'),
  client_secret = os.getenv('client_secret'),
  username = os.getenv('username'),
  password = os.getenv('password'),
  user_agent = "<CrownClown1.0>"

)

subreddit = reddit.subreddit("AskReddit+aww+conservative+conspiracy+explainlikeimfive+funny+gaming+LifeProTips+mildlyinfuriating+movies+Music+news+nottheonion+pics+politics+science+Showerthoughts+sports+todayilearned+videos+worldnews")

autism = [
"""
  No. No. No. Do I need to say this again? No. One of the most powerful pieces of evidence to show that there is no link between vaccines and autism comes from Japan where they replaced the triple vaccine Measles Mumps Rubella (MMR) with single vaccines mid-1993. Guess what happened? Autism continued to rise.

This should have been the final nail in the coffin for the autism/vaccines link but instead opponents just shifted the blame to thiomersal, the mercury-containing component that was present in small amounts in some vaccines where it was used as a preservative (MMR never contained thiomersal).

This component was removed from all scheduled childhood vaccines in the year 2000, solely because of the scary word “mercury” and not for any fears or evidence for harmful effects. If it were contributing to rising cases of autism then you would expect a dramatic drop following its removal. Instead, like the MMR in Japan, the opposite is true, and autism continues to rise.

Of course these are not the only pieces of evidence, and scientists continue to test, and re-test the safety of vaccines. A recently published exhaustive review examining 12,000 research articles covering 8 different vaccines concluded there was no link between vaccines and autism. While scientists still don’t know the exact causes of autism, we are looking like mad and one thing we can be extremely confident of is that it’s not vaccines.
""",
]

spread = [
"""
  This is a common misunderstanding particularly for the flu vaccine as many of us experience side effects following a vaccine that can easily be confused with influenza. For example, you can expect to get a sore arm at the site of injection, perhaps a slight fever, maybe a headache – symptoms synonymous with flu.

But you absolutely definitely cannot get the flu from the vaccine because there is no “live” virus in it to infect you. The mild response you get following a flu vaccine, or any vaccine for that matter, is in fact a good sign since it indicates your immune system is responding, thus the vaccine is working.

In the pages of history there are cases of vaccines causing the disease they were meant to prevent – for example in the USA in 1955, a bad batch of polio vaccine exposed several thousand children to live polio virus upon vaccination – but advances in technology and testing ensure the likelihood of this happening again is virtually zero.
""",
]

sides = [
  """
  There are two sides to the vaccine “debate” just like there are two sides to the “earth is round” debate (yes, the Flat Earth Society really does exist). On the one hand there is the scientific consensus backed by extensive research that vaccines are safe and effective, and on the other there is obfuscation, half-truths, misinformation and debunked research.

The only debate is one that has been manufactured by those with a vested interest in undermining confidence in vaccines. Those like Andrew Wakefield, who has been accused of deliberate fraud by the British Medical Journal for suggesting there was a link between the MMR and autism all the while pocketing money from lawyers tasked with suing the vaccine manufacturers.

Wakefield was also poised to submit a patent on a single measles vaccine, from which he stood to profit substantially once he’d scared everyone away from the triple antigen MMR. He also stood to make millions from a diagnostic kit he had developed for autistic enterocolitis, a new condition he claimed to have identified in his 1998 Lancet paper (which has since been retracted by the publisher). So yes, I guess there are two sides, there is the side where all the evidence lies in support of vaccination, then there are the cranks and quacks with a vested interest.
  """,
]

polio = [
  """
  Major illnesses like polio have disappeared precisely because of vaccines. Anyone heard of someone contracting smallpox recently? No? Well that’s because the last remaining supplies of smallpox now reside locked in a deep freezer in the depths of the Centres for Disease Control in Atlanta, USA. Smallpox was wiped out because of a concerted vaccination programme.

Indeed measles was also heading the same way – Australia was declared measles free in 2005 by the WHO – before we became complacent, stopped being so diligent about vaccinating and it got a chance to take hold again. The impact of not vaccinating for measles can be seen in the current epidemic in Wales where there are now over 500 cases, many of the age who missed out on their MMR vaccination following the famous 1998 Andrew Wakefield scare.

In Australia in 2010, doctors were shocked by the death of a 22 year old who died from diphtheria, a disease now unheard of, after contracting it from a friend who caught it during an overseas holiday. It is believed she wasn’t vaccinated against the bacterial infection.

In many ways, vaccines are a victim of their own success, since they create an “out-of-mind, out-of-sight” scenario lulling us into a false sense of security. We don’t see kids in calipers anymore, or hospitals full of iron lungs, but if we stop vaccinating then we create an environment where they can return.
  """,
]

overwhelm = [
  """
  The concept of “too many too soon” has been championed by celebrity Mom Jenny McCarthy and Dr Bob Spears, and as a result has been the subject of intense scrutiny by scientists. Very recently a detailed analysis of the US childhood immunisation schedule was conducted to look for any deleterious effects of the number of vaccines kids receive.

The Institute of Medicine specifically looked for evidence that vaccination is linked to “autoimmune diseases, asthma, hypersensitivity, seizures, child developmental disorders, learning or developmental disorders, or attention deficit or disruptive disorders”, including autism. They confirmed what other researchers have also observed, that the childhood schedule is safe.

With respect to overwhelming kids’ immune systems, the tiny amount of antigens in vaccines pales in to comparison to what they are exposed to every day via playing, eating and drinking. The amount of immune challenges that children fight every day (2,000 — 6,000) in the environment is significantly greater than the number of antigens or reactive particles in all their vaccinations combined (about 150 for the entire vaccination schedule).

Also, because of innovations in the way vaccines are made, today’s vaccines contain far fewer antigens than those administered in the past. The new pertussis vaccine for example has significantly less antigens than the older style “whole cell” vaccine meaning it causes fewer side effects (but that it is also less effective).
  """,
]

nanotech = [
  "The vaccine contains very few ingredients. One of them being mRNA, which is the active ingredient in the vaccine, in addition to lipids salts and sugars, which are included to stabilize that mRNA. Other than that, there are no microchips, and there is no chance of anyone being able to trace you as a result of receiving this vaccine.",
]

hoax = [
  """
  "I think I made a mistake. I thought this was a hoax, but it's not." Those were some of the last words uttered by a 30-year-old Texas man who attended a "coronavirus party" thinking Covid-19 was a hoax.
  """
]

jokes = [
  """
  A friend of mine went to take the vaccine for covid yesterday
After getting vaccinated, his vision was blurred and when he reached home, he called the hospital that gave him the vaccine for advice asking if he should be hospitalized.

The hospital told him to come back and collect his glasses
  """,
  """
  Person: How do you feel about those anti-vaxxers using your illness / genetic disorder to promote their agenda?

  Autist:

  I don't mind it. Being autistic isn't all that bad compared to being an idiot.
  """,
  """
  People say "well what did people do before vaccines?" as if that's an argument for going natural.

  They died, Carol. A lot of people died.
  """, 
  "[Your comment reminds me of this picture](https://imgur.com/a/iwrznMR)",
  "[Your comment reminds me of this picture](https://imgur.com/a/ctNuhxk",
  "[Your comment reminds me of this picture](https://imgur.com/a/ny11ks0",
  "[Your comment reminds me of this picture](https://imgur.com/a/nFHOuNX",
  "[Your comment reminds me of this picture](https://imgur.com/a/IYHJAUr",
  "[Your comment reminds me of this picture](https://imgur.com/a/aphyveb",
  "[Your comment reminds me of this picture](https://imgur.com/a/rVwTQaI",
  "[Your comment reminds me of this picture]https://imgur.com/a/VRFhN6f",
  "[Your comment reminds me of this picture]https://imgur.com/a/wpjn81X",
  "[Your comment reminds me of this picture]https://imgur.com/a/dSbofaa",
  "[Your comment reminds me of this picture]https://imgur.com/a/Bip6sET",
  "[Your comment reminds me of this picture]https://imgur.com/a/4asCHq8",
  "[Your comment reminds me of this picture]https://imgur.com/a/T7Irvzi",
  "[Your comment reminds me of this picture]https://imgur.com/a/Q1p7IIf",
  "[Your comment reminds me of this picture]https://imgur.com/a/ROCrmvC",
  "[Your comment reminds me of this picture]https://imgur.com/a/SC6qmgc",
  "[Your comment reminds me of this picture]https://imgur.com/a/DmeD2Xa",
  "[Your comment reminds me of this picture]https://imgur.com/a/G3dJPTK",
  "[Your comment reminds me of this picture]https://imgur.com/a/ng5kniv",
  "[Your comment reminds me of this picture]https://imgur.com/a/VHqLtjU",




]

trigger_list = [
  "i am anti-vax",
  "vaccines cause autism",
  "fuck the vax",
  "don't take the vax",
]

for comment in subreddit.stream.comments(skip_existing=True):
  if comment.author.name != "EvanRobinsontry" and comment.author.name != "None":
    if " vaccines cause autism " in comment.body:
      print("----------------------")
      print(comment.body)
      comment.reply(autism[0])
    if " vaccines spread covid " in comment.body:
      print("----------------------")
      print(comment.body)
      comment.reply(spread[0])
    if " there are two sides " in comment.body:
      print("----------------------")
      print(comment.body)
      comment.reply(sides[0])
    if " polio is gone " in comment.body:
      print("----------------------")
      print(comment.body)
      comment.reply(polio[0])
    if " vaccines overwhelm " in comment.body:
      print("----------------------")
      print(comment.body)
      comment.reply(overwhelm[0])
    if " harmful nanotechnology " in comment.body:
      print("----------------------")
      print(comment.body)
      comment.reply(nanotech[0])
    if " corona is a hoax " in comment.body:
      print("----------------------")
      print(comment.body)
      comment.reply(hoax[0])
    if " vax " in comment.body or " vaccine " in comment.body:
      print("----------------------")
      print(comment.body)
      comment.reply(jokes[0])


