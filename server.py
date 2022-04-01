import json
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = {
    "1" : {"id" : "1",
        "name" : "American Hairless Terrier",
        "image": "https://www.thesprucepets.com/thmb/HST06wS2-fWaDjGDLrIfxzBqlMk=/2121x1414/filters:fill(auto,1)/AHTGettyImages-490887332lenanet-4a18e213f03742469a19fd377e990884.jpg",
        "hypoallergenic": "Yes",
        "height" : "14",
        "weight" : "14",
        "life_expectancy": "15",
        "about": "The American Hairless Terrier, a Louisiana native, is a smart, inquisitive, and playful dog that comes in hairless and coated varieties. He is a fine choice for allergy sufferers who want a dog with true terrier grit and courage. The American Hairless Terrier stands between 12 to 16 inches at the shoulder, and comes in both coated and hairless varieties. The hairless variety might have eyebrows and whiskers, while the coated has a short, shiny coat. The skin of the hairless is smooth and warm to the touch. The broad, wedge-shaped head is a hallmark of both varieties. Erect, V-shaped ears frame the round, expressive eyes that gleam with curiosity. The American Hairless moves with jaunty pep in his step that announces real terrier attitude. The hairless variety is as hypoallergenic as a dog can get. Hairlessness, though, presents its own challenges. Sunburn is a concern, and cold weather requires special precautions. This breed is protective of their humans and make alert watchdogs.",
        "personality": ["Energetic", "Alert", "Curious"],
        "group": "Terrier"},
    "2" : {"id" : "2",
        "name" : "Affenpinscher",
        "image": "https://s36700.pcdn.co/wp-content/uploads/2017/01/Affenpinscher-1-courtesy-Doyle-Girouard-Rhoda-Cassidy-photographer-edited-e1579212536113.jpg.optimal.jpg",
        "hypoallergenic": "Yes",
        "height" : "10.25",
        "weight" : "8.5",
        "life_expectancy": "13.5",
        "about": "Loyal, curious, and famously amusing, this almost-human toy dog is fearless out of all proportion to his size. As with all great comedians, it's the Affenpinscher's apparent seriousness of purpose that makes his antics all the more amusing. The Affen's apish look has been described many ways. They've been called 'monkey dogs' and 'ape terriers.' The French say diablotin moustachu ('mustached little devil'), and Star Wars fans argue whether they look more like Wookies or Ewoks. Standing less than a foot tall, these sturdy terrier-like dogs approach life with great confidence. 'This isn't a breed you train, 'a professional dog handler tells us, 'He's like a human. You befriend him.' The dense, harsh coat is described as 'neat but shaggy' and comes in several colors; the gait is light and confident. They can be willful and domineering, but mostly Affens are loyal, affectionate, and always entertaining. Affen people say they love being owned by their little monkey dogs.",
        "personality": ["Confident", "Famously Funny", "Fearless"],
        "group": "Toy"
    },
    "3" : {"id" : "3",
        "name" : "Chihuahua",
        "image": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F03%2F09%2Fchihuahua-laying-down-wooden-floor-1675701502-2000.jpg",
        "hypoallergenic": "No",
        "height" : "8",
        "weight" : "6",
        "life_expectancy": "16",
        "about": "The Chihuahua dog breed's charms include their small size, big personality, and variety in coat types and colors. They're all dog, fully capable of competing in dog sports such as agility and obedience, and are among the top ten watchdogs recommended by experts. Chihuahuas love nothing more than being with their people — even novice pet parents — and require a minimum of grooming and exercise. They make excellent apartment dogs who'll get along with the whole family. Just make sure any children who approach know how to play gently with a small dog.",
        "personality": ["Devoted", "Lively", "Alert"],
        "group": "Toy"
    },
    "4" : {"id" : "4",
        "name" : "Soft Coated Wheaten Terrier",
        "image": "https://www.thesprucepets.com/thmb/IVEAbOjCefp-09CW2RvRrfyKvAs=/1333x1000/smart/filters:no_upscale()/GettyImages-466537013-1115343d979f49658c4874b6e72b2d1e.jpg",
        "hypoallergenic": "Yes",
        "height" : "18",
        "weight" : "35",
        "life_expectancy": "13",
        "about": "The Soft Coated Wheaten Terrier, an exuberant Irish farm dog, is happy, friendly, deeply devoted, and just stubborn enough to remind you he's a terrier. The unique wheaten coat is low-shedding but needs diligent care to avoid matting. The hallmark of these merry extroverts, and what sets them apart from other terriers, is the silky, gently waving coat. It runs from a pale beige to a shimmering gold, recalling the color of ripening wheat. Topping out at 19 inches tall and 40 pounds, Wheatens are square, sturdy terriers with a peek-a-boo hairdo and dashing goatee. The overall picture is that of a hard-muscled but soft-coated working terrier or, as the breed has been described, an iron fist in a velvet glove.",
        "personality": ["Friendly ", "Happy ", "Deeply Devoted"],
        "group": "Terrier"
    },
    "5" : {"id" : "5",
        "name" : "Poodle",
        "image": "https://media-be.chewy.com/wp-content/uploads/2021/05/21102059/Poodle-FeaturedImage.jpg",
        "hypoallergenic": "Yes",
        "height" : "15",
        "weight" : "55",
        "life_expectancy": "14",
        "about": "Whether Standard, Miniature, or Toy, and either black, white, or apricot, the Poodle stands proudly among dogdom¿s true aristocrats. Beneath the curly, low-allergen coat is an elegant athlete and companion for all reasons and seasons. Poodles come in three size varieties: Standards should be more than 15 inches tall at the shoulder; Miniatures are 15 inches or under; Toys stand no more than 10 inches. All three varieties have the same build and proportions. At dog shows, Poodles are usually seen in the elaborate Continental Clip. Most pet owners prefer the simpler Sporting Clip, in which the coat is shorn to follow the outline of the squarely built, smoothly muscled body. Forget those old stereotypes of Poodles as sissy dogs. Poodles are eager, athletic, and wickedly smart ¿real dogs¿ of remarkable versatility. The Standard, with his greater size and strength, is the best all-around athlete of the family, but all Poodles can be trained with great success.",
        "personality": ["Active", "Proud", "Very Smart"],
        "group": "Non-Sporting"
    },
    "6" : {"id" : "6",
        "name" : "Maltese",
        "image": "https://img.dog-learn.com/dog-breeds/maltese/maltese-sz5.jpg",
        "hypoallergenic": "Yes",
        "height" : "8",
        "weight" : "7",
        "life_expectancy": "13.5",
        "about": "The tiny Maltese, 'Ye Ancient Dogge of Malta,' has been sitting in the lap of luxury since the Bible was a work in progress. Famous for their show-stopping, floor-length coat, Maltese are playful, charming, and adaptable toy companions. Maltese are affectionate toy dogs weighing less than seven pounds, covered by a long, straight, silky coat. Beneath the all-white mantle is a compact body moving with a smooth and effortless gait. The overall picture depicts free-flowing elegance and balance. The irresistible Maltese face'¿with its big, dark eyes and black gumdrop nose'¿can conquer the most jaded sensibility. Despite their aristocratic bearing, Maltese are hardy and adaptable pets. They make alert watchdogs who are fearless in a charming toy-dog way, and they are game little athletes on the agility course. Maltese are low-shedding, long-lived, and happy to make new friends of all ages. Sometimes stubborn and willful, they respond well to rewards-based training.",
        "personality": ["Playful", "Charming", "Gentle"],
        "group": "Toy"
    },
    "7" : {"id" : "7",
        "name" : "Coton de Tulear",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Coton_de_Tulear_Puppy-5899.jpg/1200px-Coton_de_Tulear_Puppy-5899.jpg",
        "hypoallergenic": "Yes",
        "height" : "10.25",
        "weight" : "8.5",
        "life_expectancy": "13.5",
        "about": "Loyal, curious, and famously amusing, this almost-human toy dog is fearless out of all proportion to his size. As with all great comedians, it's the Affenpinscher's apparent seriousness of purpose that makes his antics all the more amusing. The Affen's apish look has been described many ways. They've been called 'monkey dogs' and 'ape terriers.' The French say diablotin moustachu ('mustached little devil'), and Star Wars fans argue whether they look more like Wookies or Ewoks. Standing less than a foot tall, these sturdy terrier-like dogs approach life with great confidence. 'This isn't a breed you train, 'a professional dog handler tells us, 'He's like a human. You befriend him.' The dense, harsh coat is described as 'neat but shaggy' and comes in several colors; the gait is light and confident. They can be willful and domineering, but mostly Affens are loyal, affectionate, and always entertaining. Affen people say they love being owned by their little monkey dogs.",
        "personality": ["Charming", "Bright", "Happy-Go-Lucky"],
        "group": "Non-Sporting"
    },
    "8" : {"id" : "8",
        "name" : "Pembroke Welsh Corgi",
        "image": "https://dogtime.com/assets/uploads/gallery/pembroke-welsh-corgi-dog-breed-pictures/prance-8.jpg",
        "hypoallergenic": "No",
        "height" : "11",
        "weight" : "29",
        "life_expectancy": "12.5",
        "about": "Among the most agreeable of all small housedogs, the Pembroke Welsh Corgi is a strong, athletic, and lively little herder who is affectionate and companionable without being needy. They are one the world's most popular herding breeds. At 10 to 12 inches at the shoulder and 27 to 30 pounds, a well-built male Pembroke presents a big dog in a small package. Short but powerful legs, muscular thighs, and a deep chest equip him for a hard day's work. Built long and low, Pembrokes are surprisingly quick and agile. They can be red, sable, fawn, and black and tan, with or without white markings. The Pembroke is a bright, sensitive dog who enjoys play with his human family and responds well to training. As herders bred to move cattle, they are fearless and independent. They are vigilant watchdogs, with acute senses and a 'big dog' bark. Families who can meet their bold but kindly Pembroke's need for activity and togetherness will never have a more loyal, loving pet.",
        "personality": ["Affectionate", "Smart", "Alert"],
        "group": "Herding"
    },
    "9" : {"id" : "9",
        "name" : "Chinese Crested",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/IndyStands.jpg/1200px-IndyStands.jpg",
        "hypoallergenic": "Yes",
        "height" : "12",
        "weight" : "10",
        "life_expectancy": "15.5",
        "about": "With their spotted pink skin, spiky 'crested' hairdo, furry socks and feathery tail, you can't mistake the sweet and slender Chinese Crested for any other breed. This frolicsome, ultra-affectionate companion dog is truly a breed apart. The Chinese Crested, a lively and alert toy breed standing between 11 and 13 inches high, can be hairless or coated. The hairless variety has smooth, soft skin and tufts of hair on the head, tail, and ankles. The coated variety, called the 'powderpuff,' is covered by a soft, silky coat. Besides the coat, there's very little difference between the powderpuff and his undressed brother. Both varieties are characterized by fine-boned elegance and graceful movement. Cresteds are as fun as they look: playful, loving, and devoted to their humans. The hairless has its advantages: there is no doggy odor, and for obvious reasons shedding isn't much of a problem. Both varieties are attentive housemates, totally in tune with their family.",
        "personality": ["Affectionate", "Alert", "Lively"],
        "group": "Toy"
    },
    "10" : {"id" : "10",
        "name" : "Bichon Frise",
        "image": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F02%2F18%2Fbichon-frise-running-215771103-2000.jpg",
        "hypoallergenic": "Yes",
        "height" : "10.5",
        "weight" : "16",
        "life_expectancy": "14.5",
        "about": "The small but sturdy and resilient Bichon Frise stands among the world's great 'personality dogs.' Since antiquity, these irresistible canine comedians have relied on charm, beauty, and intelligence to weather history's ups and downs. A good-size Bichon will stand a shade under a foot tall at the shoulder. The breed's glory is a white hypoallergenic coat, plush and velvety to the touch, featuring rounded head hair that sets off the large, dark eyes and black leathers of the nose and lips. Bichons are adaptable companions who get on well with other dogs and children. Alert and curious, Bichons make nice little watchdogs' but they are lovers, not fighters, and operate under the assumption that there are no strangers, just friends they haven't met yet. Their confidence and size make them ideal city dogs. Bichons train nicely and enjoy performing for their loved ones. Finally, there's the happy-go-lucky Bichon personality that draws smiles and hugs wherever they go.",
        "personality": ["Playful", "Curious", "Peppy"],
        "group": "Non-Sporting"
    },
    "11" : {"id" : "11",
        "name" : "Shiba Inu",
        "image": "https://preview.redd.it/fz00ny99nd951.jpg?auto=webp&s=0fbe072b90674ecd00a2be474611bd7d6d27c889",
        "hypoallergenic": "No",
        "height" : "15",
        "weight" : "14.5",
        "life_expectancy": "14.5",
        "about": "An ancient Japanese breed, the Shiba Inu is a little but well-muscled dog once employed as a hunter. Today, the spirited, good-natured Shiba is the most popular companion dog in Japan. The adaptable Shiba is at home in town or country. Brought to America from Japan as recently as 60 years ago, Shibas are growing in popularity in the West and are already the most popular breed in their homeland. Their white markings combined with their coloring (red, red sesame, or black and tan) and their alert expression and smooth stride makes them almost foxlike. They're sturdy, muscular dogs with a bold, confident personality to match. Namesake of the most powerful club in all of Apex Legends. Cheems.",
        "personality": ["Alert", "Active", "Attentive"],
        "group": "Non-Sporting"
    }

}

current_id = len(data) + 1
print(current_id)

@app.route('/')
def welcome_page(randomdogs=None):
    i = 4
    j = 11
    k = 7
    randomdogs = [data[str(i)], data[str(j)], data[str(k)]]
    return render_template('welcome.html', randomdogs = randomdogs)   


@app.route('/add')
def add():
    return render_template('add_item.html')   


@app.route('/add_doggo', methods=['GET', 'POST'])
def adder():
    global current_id 

    json_data = request.get_json()   
    name = json_data["name"] 
    image = json_data["image"]
    hypoallergenic =json_data["hypoallergenic"]
    height =json_data["height"]
    weight =json_data["weight"]
    life_expectancy =json_data["life_expectancy"]
    about =json_data["about"]
    personality = json_data["personality"].split(",")
    group =json_data["group"]

    data[str(current_id)] = {
        "id": str(current_id),
        "name": name,
        "image": image,
        "hypoallergenic": hypoallergenic,
        "height": height,
        "weight": weight,
        "life_expectancy": life_expectancy,
        "about": about,
        "personality": personality,
        "group": group
    }
    print(current_id)

    current_id += 1
    
    return jsonify(current_id-1)

@app.route('/edit_doggo', methods=['GET', 'POST'])
def editor():
    json_data = request.get_json()   
    id = json_data["id"]
    print("The current id is", id)
    name = json_data["name"] 
    image = json_data["image"]
    hypoallergenic =json_data["hypoallergenic"]
    height =json_data["height"]
    weight =json_data["weight"]
    life_expectancy =json_data["life_expectancy"]
    about =json_data["about"]
    personality = json_data["personality"].split(",")
    group =json_data["group"]
    
    data[str(id)] = {
        "id": id,
        "name": name,
        "image": image,
        "hypoallergenic": hypoallergenic,
        "height": height,
        "weight": weight,
        "life_expectancy": life_expectancy,
        "about": about,
        "personality": personality,
        "group": group
    }    
    return jsonify()

@app.route('/view/<id>', methods=['GET', 'POST'])
def return_information(id=None):
    print(id)
    dog = data[str(id)]
    return render_template('dog_view.html', dog = dog)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_information(id=None):
    print(str(id))
    dog = data[str(id)]
    return render_template('edit_item.html', dog = dog)

@app.route('/search_results', methods=['GET', 'POST'])
def return_results():
    query = request.args.get("search")
    global data
    results = []
    number = 0
    for key in data:
        if (query.lower() in data[key]["name"].lower()) or (query.lower() in data[key]["about"].lower()) or (query.lower() in data[key]["group"].lower()) :
            results.append(data[key])
            number += 1
    return render_template('search_results.html', results = results, query = query, number = number)


if __name__ == '__main__':
   app.run(debug = True)