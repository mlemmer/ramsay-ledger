class LedgerItem(object):
    def __init__(self, title, description, image, materials, dimensions, distance, collection, link, page, department, pounds, dollars, license=None, artifact=None, date=None, origin=None, analytics=None, customer=None, ledger=None):
        self.title = title
        self.description = description
        self.image = image
        self.materials = materials
        self.dimensions = dimensions
        self.distance = distance
        self.collection = collection
        self.link = link
        self.page = page
        self.department = department
        self.pounds = pounds
        self.dollars = dollars
        self.license = license
        self.artifact = artifact
        self.date = date
        self.origin = origin
        self.analytics = analytics
        self.customer = customer
        self.ledger = ledger

FAKE_DB = {
    "Mug": LedgerItem(
        title="Stoneware Mug",
        description="William Ramsay owned the Fairfax, a vessel he unsuccessfully tried to sell in 1751. The ship had its own ledger account that listed this mug and other provisions needed to maintain the vessel at sea",
        image="Mug2.jpg",
        materials="Stoneware",
        dimensions="Unknown",
        distance="Unknown",
        collection="Smithsonian",
        link="NA",
        page="160",
        department="Dining",
        pounds="9d",
        dollars="Unknown",
        artifact="Green Stoneware Mug",
        date="18th century",
        origin="Unknown",
        customer="The Brigantine Fairfax",
        ledger="MugLedger.jpg",
        analytics=""),

    "Gloves": LedgerItem(
        title="Gloves",
        description="In 1753, Capt. Lewis Ellzey purchased a pair of 'women's coloured gloves' as well as two pairs of 'women's tabby breasted stays,' a pair of 'Women's fine white worsted hose,' and a pair of child's stays, indicating that items for his whole family were purchased on his account",
        image="Gloves.jpg",
        materials="Leather",
        dimensions="Unknown",
        distance="Unknown",
        collection="Smithsonian",
        link="NA",
        page="30",
        department="Outerwear",
        pounds="15d",
        dollars="Unknown",
        artifact="Blue-Green Women's Gloves",
        date="Early 19th Century",
        origin="Unknown",
        customer="Captain Lewis Ellzey",
        ledger="GlovesLedger.jpg",
        analytics="There are 29 pairs of gloves in the Ramsay database with prices ranging from 10 pence for womens washing gloves to 6 shillings for buckskin gloves.",),

    "Ribbon": LedgerItem(
        title="Ribbon",
        description="Blue-Green ribbon with brown and green stripes, late 18th century. Ribbons had many uses. They were an affordable way for women to update an older garment, to trim a hat, or to tie up their hair. During a period when men and women were bound by many rules of proper behavior, ribbons were an appropriate gift to show romantic interest",
        image="Ribbon.jpg",
        materials="Satin",
        dimensions="Unknown",
        distance="Unknown",
        collection="Smithsonian",
        link="NA",
        page="77",
        department="Trim",
        pounds="10d",
        dollars="Unknown"),

    "Shoes": LedgerItem(
        title="Women's Best Shoes",
        description="Ivory shoes with embroidered paterns, 18th century. William Ramsay imported shoes for his customers. In August 1753, Vorlinda Wade purchased eight pairs of 'best shoes,' from Ramsay. Wade was a widow and the sole owner of a 193-acre tobacco farm that adjoined George Washington's Alexandria, Virginia, property.",
        image="Shoes.jpg",
        materials="Satin",
        dimensions="Unknown",
        distance="Unknown",
        collection="Smithsonian",
        link="NA",
        page="126",
        department="Footwear",
        pounds="3s, 6d",
        dollars="Unknown"),

    "BoheaTea": LedgerItem(
        title="Bohea Tea",
        description="A category of black and oolong teas imported from the Wuyi Mountains of northern Fujian, China.",
        image="BoheaTea.jpg",
        materials="Black and Oolong teas",
        dimensions="Unknown",
        distance="12,592 km",
        collection="Image by Lateasquirrel",
        link="https://commons.wikimedia.org/wiki/File:Da_Hong_Pao_Oolong_tea_leaf.jpg",
        page="106",
        department="Beverages",
        pounds="3s, 3d",
        dollars="Unknown",
        license="GNU Free Documentation License"),
    
    "Cinnamon": LedgerItem(
        title="Cinnamon",
        description=" a spice obtained from the inner bark of several trees from the genus Cinnamomum that is used in both sweet and savoury foods.",
        image="Cinnamon.jpg",
        materials="Cinnamon bark",
        dimensions="Unknown",
        distance="Unknown",
        collection="Image by Bertrand THIRY",
        link="https://en.wikipedia.org/wiki/Cinnamon#/media/File:Baton_de_cannelle.jpg",
        page="92",
        department="Spices",
        pounds="12d",
        dollars="Unknown",
        license="CC BY-SA"),

    "Ginger": LedgerItem(
        title="Ginger",
        description="Ginger (Zingiber officinale Roscoe) is a flowering plant, in the family Zingiberaceae whose rhizome, ginger root or simply ginger, is widely used as a spice or a folk medicine.",
        image="Ginger.jpg",
        materials="Ginger Root",
        dimensions="Unknown",
        distance="Unknown",
        collection="Image by Foaunrw",
        link="https://commons.wikimedia.org/wiki/Category:Ginger#/media/File:IngwerXYZ_0004.jpg",
        page="125",
        department="Spices",
        pounds="7d",
        dollars="Unknown",
        license="CC BY-SA"),

    "Salt": LedgerItem(
        title="Salt",
        description="A mineral composed primarily of sodium chloride (NaCl), a chemical compound belonging to the larger class of salts. Salt is one of the oldest and most ubiquitous of food seasonings, and salting is an important method of food preservation. In William Ramsay's store, salt was sold by the bushel, or in 50lb increments.",
        image="Salt.jpg",
        materials="Salt",
        dimensions="Unknown",
        distance="Unknown",
        collection="Image by Dubravko Soric",

#       accent needed on the c of Soric

        link="https://www.flickr.com/photos/11939863@N08/3794105536",
        page="124",
        department="Spices",
        pounds="1s, 4d",
        dollars="Unknown",
        license="CC BY-SA"),

    "Allspice": LedgerItem(
        title="Allspice",
        description="The dried unripe fruit (berries, used as a spice) of Pimenta dioica, a midcanopy tree native to the Greater Antilles, southern Mexico, and Central America, now cultivated in many warm parts of the world. The name 'allspice' was coined as early as 1621 by the English, who thought it combined the flavour of cinnamon, nutmeg, and cloves.",
        image="Allspice.jpg",
        materials="Allspice",
        dimensions="Unknown",
        distance="1,922 km",
        collection="Image by Jonathunder",
        link="https://commons.wikimedia.org/wiki/Category:Allspice#/media/File:WholeAllspice.JPG",
        page="92",
        department="Spices",
        pounds="1s, 1.5d",
        dollars="Unknown",
        license="CC BY-SA"),

    "Cloves":LedgerItem(
        title="Cloves",
        description="The aromatic flower buds of a tree in the family Myrtaceae, Syzygium aromaticum. They are native to the Maluku Islands in Indonesia, and are commonly used as a spice. Cloves are commercially harvested primarily in Bangladesh, Indonesia, India, Madagascar, Zanzibar, Pakistan, Sri Lanka and Tanzania.",
        image="Cloves.jpg",
        materials="Cloves",
        dimensions="Unknown",
        distance="15,188 km",
        collection="Image by Henna",
        link="https://commons.wikimedia.org/wiki/File:Cloves-spice.jpg",
        page="129",
        department="Spices",
        pounds="14d",
        dollars="Unknown",
        license="CC BY-SA"),

    "Nutmeg":LedgerItem(
        title="Nutmeg",
        description="One of the two spices, the other being mace, derived from several species of tree in the genus Myristica. Nutmeg is the seed of the tree, roughly egg-shaped. Nutmeg is usually used in powdered form.",
        image="Nutmeg.jpg",
        materials="Nutmeg",
        dimensions="Unknown",
        distance="15,633 km",
        collection="Image by Dominikmatus",
        link="https://commons.wikimedia.org/wiki/File:Nutmeg-spice.jpg",
        page="92",
        department="Spices",
        pounds="12d",
        dollars="Unknown",
        license="CC0 1.0"),

    "Molasses":LedgerItem(
        title="Molasses",
        description="A viscous by-product of the refining of sugarcane or sugar beets into sugar. Molasses varies by amount of sugar and method of extraction, and age of plant. On Feb. 2, 1756, William Baker was charged 3 shillings for 2 gallons of molasses. On June 30, 1756 Charles Mason was charged 6 shillings for the same quantity of molasses. This discrepancy in cost could stem from a number of causes including preferential treatment of customers, marken influences, or seasonal availability.",
        image="Molasses.jpg",
        materials="Molasses",
        dimensions="Unknown",
        distance="Unknown",
        collection="Image by Badagnani",
        link="https://commons.wikimedia.org/wiki/Category:Molasses#/media/File:Blackstrapmolasses.JPG",
        page="400, 361",
        department="Sweetener",
        pounds="3s or 6s",
        dollars="Unknown",
        license="CC BY 3.0"),

    "Sugar":LedgerItem(
        title="Sugar",
        description="A sweetener derived typically from sugarcane. A great expansion in its production took place in the 18th century with the establishment of sugar plantations in the West Indies and Americas. This was the first time that sugar became available to the common people, who had previously had to rely on honey to sweeten foods.",
        image="Sugar.jpg",
        materials="Sugar",
        dimensions="Unknown",
        distance="Unknown",
        collection="Image by Editor at Large",
        link="https://en.wikipedia.org/wiki/Sugar#/media/File:Raw_sugar_closeup.jpg",
        page="29",
        department="Sweetener",
        pounds="9d for 2 lbs",
        dollars="Unknown",
        license="CC BY-SA"),

    "SugarLoaf":LedgerItem(
        title="Double Refined Sugar Loaf",
        description="A sugarloaf was the traditional form in which refined sugar was produced and sold until the late 19th century when granulated and cube sugars were introduced. A tall cone with a rounded top was the end-product of a process that saw the dark molasses-rich raw sugar, which was imported from sugar cane growing regions such as the Caribbean and Brazil, refined into white sugar. The quantity of sugar per loaf is not consistant in the Ramsay ledger, rather the clerk noted the weight for each sale. On March 22, 1754 Nathanial Smith purchased a loaf of double refined sugar weighing 3lbs 10oz for 2 shillings.",
        image="SugarLoaf.jpg",
        materials="Sugar",
        dimensions="Unknown",
        distance="Unknown",
        collection="Image by Petr Adam Dohnalek",
##      accute accent on a in Dohnalek
        link="https://en.wikipedia.org/wiki/Sugar#/media/File:Raw_sugar_closeup.jpg",
        page="111",
        department="Sweetener",
        pounds="2s",
        dollars="Unknown",
        license="CC BY-SA"),



    "Buckles1":LedgerItem(
        title="Shoe Buckle",
        description="Simple unadorned steel shoe buckle. While shoe buckles did serve as fashion accessories for both men and women, this unadorned buckle reflects the more practical use of buckles to fasten shoes.",
        image="ShoeBuckle.jpg",
        materials="Steel",
        dimensions="2 1/4 x 2 3/4 in.",
        distance="Unknown",
        collection="LACMA",
        link="http://collections.lacma.org/node/246563",
        page="272",
        department="Footwear",
        pounds="10d",
        dollars="Unknown",
        license="Public Domain"),

    "Buckles2":LedgerItem(
        title="Men's Best Steel Shoe Buckles",
        description="Steel shoe buckles with floral and geometric patterns. Shoe buckles are fashion accessories worn by men and women from the mid-17th century through the 18th century. Shoe buckles were made of a variety of materials including brass, steel, silver or silver gilt, and buckles for formal wear were set with diamonds, quartz or imitation jewels.",
        image="ShoeBuckle2.jpg",
        materials="Pewter, steel",
        dimensions="2 5/8 x 2 in",
        distance="Produced in the United States",
        collection="LACMA",
        link="http://collections.lacma.org/node/228165",
        page="30",
        department="Footwear",
        pounds="1s, 10d",
        dollars="Unknown",
        license="Public Domain"),

    "Buckles3":LedgerItem(
        title="Men's Breeches Buckles",
        description="Breeches were an article of mens clothing covering the body from the waist down. The breeches could be closed and fastened by either buttons or by a draw-string, but in the Eighteenth century, decorated buckles such as these were used both the fasten the breeches and as fashion accessories",
        image="BreechesBuckle.jpg",
        materials="Metal",
        dimensions="1 x 1 1/2 in.",
        distance="Unknown",
        collection="LACMA",
        link="http://collections.lacma.org/node/176035",
        page="176",
        department="Accessories",
        pounds="5d",
        dollars="Unknown",
        license="Public Domain"),

    "Petticoat":LedgerItem(
        title="Woman's Petticoat",
        description="Blue linsey woolsey, wool, quilted and stuffed. A petticoat or underskirt is an undergarment to be worn under a skirt or a dress. The petticoat is a separate garment hanging from the waist. While Ramsay's store did not sell many completed garments, 'petticoating' fabric was sold for women to make their petticoats.",
        image="Petticoat.jpg",
        materials="Wool",
        dimensions="33 1/2 x 102 in.",
        distance="Produced in the United States",
        collection="LACMA",
        link="http://collections.lacma.org/node/171379",
        page="38",
        department="Underwear",
        pounds="2s, 9d",
        dollars="Unknown",
        license="Public Domain"),

    "Hoop":LedgerItem(
        title="Small Cane Hoop Petticoat",
        description="On Sept. 27, 1753 Mrs. Sarah Wigginton purchased a 'small cane hoop' for 4 shillings. While this description is vague and could refer possibly to a hoop for needlecraft or a hoop for children's games, it could also refer to a type of undergarment which uses cane or whalebone hoops to give fullness to a woman's skirts. The durability and flexibility of whalebone made it the prefered material for this purpose, but its scarcity made it more expensive. Cane was used as a more economical alternative.",
        image="Hoop.jpg",
        materials="Linen plain weave and cane",
        dimensions="31 1/4 x 54 x 18 1/2 in.",
        distance="3,607 mi",
        collection="LACMA",
        link="http://collections.lacma.org/node/214714",
        page="19",
        department="Underwear",
        pounds="4s",
        dollars="Unknown",
        license="Public Domain"),

    "Stays":LedgerItem(
        title="Women's Stays",
        description="Blue stays with gold trim from England. Stays are a form of undergarment worn primarily by women and children which utilize stiff boning to alter the wearer's posture and body shape.",
        image="Stays.jpg",
        materials="Silk moire, silk cording and ribbons, linen lining",
        dimensions="Center back length: 15 in.",
        distance="3,607 mi",
        collection="LACMA",
        link="http://collections.lacma.org/node/232498",
        page="111",
        department="Underwear",
        pounds="51s, 6d",
        dollars="Unknown",
        license="Public Domain"),

    "Damask":LedgerItem(
        title="Damask",
        description="Red Brocaded wool damask panel. Damask is a reversible figured fabric of silk, wool, linen, cotton, or synthetic fibres, with a pattern formed by weaving. Damasks are woven with one warp yarn and one weft yarn, usually with the pattern in warp-faced satin weave and the ground in weft-faced or sateen weave.",
        image="Damask.jpg",
        materials="Wool",
        dimensions="38 x 18 in.",
        distance="Unknown",
        collection="LACMA",
        link="http://collections.lacma.org/node/233912",
        page="195",
        department="Textile",
        pounds="1s, 8d",
        dollars="Unknown",
        license="Public"),

    "Primer":LedgerItem(
        title="New-England Primer",
        description="Both Hugh West Jr. and Thomas Self purchased unspecified primers from the Ramsay store. The New England Primer was the first reading primer designed for the American Colonies. It became the most successful educational textbook published in 18th century America and it became the foundation of most schooling before the 1790s. In the 17th century, the schoolbooks in use had been brought over from England. By 1690, Boston publishers were reprinting the English Protestant Tutor under the title of The New England Primer. The Primer included additional material that made it widely popular with colonial schools until it was supplanted by Noah Webster's Blue Back Speller after 1790.",
        image="Primer.jpg",
        materials="Book",
        dimensions="Unknown",
        distance="128.15 miles",
        collection="Beinecke Rare Book & Manuscript Library, Yale University",
        link="https://commons.wikimedia.org/wiki/File:New-England_Primer_Enlarged_printed_and_sold_by_Benjamin_Franklin.jpgTh",
        page="83, 222",
        department="Literacy",
        pounds="6d",
        dollars="Unknown",
        license="Public Domain"),

    "Bottle":LedgerItem(
        title="Ink Bottle",
        description="On Dec 6, 1753 Henry Vanmetre purchased an 'Ink Holder' for 7.5 pence. While this term is vague, it likely refered to an ink bottle such as this salt glazed stoneware ink bottle at the Bedford Museum.",
        image="Inkholder.jpg",
        materials="Stoneware",
        dimensions="Unknown",
        distance="Unknown",
        collection="Bedford Museum, image by Simon Speed",
        link="https://commons.wikimedia.org/wiki/File:StonewareInkBottleBedfordMuseum.JPG",
        page="258",
        department="Literacy",
        pounds="7.5d",
        dollars="Unknown",
        license="Public Domain"),

    "Hat":LedgerItem(
        title="Men's Fine Hat",
        description="Black men's tricorne beaver fur hat. The tricorne or tricorn is a style of hat that was popular during the 18th century, falling out of style by 1800. During the 18th century hats of this general style were referred to as 'cocked hats'. At the peak of its popularity, the cocked hat (tricorne) varied greatly in style and size, and was worn not only by the aristocracy, but also as common civilian dress, and as part of military and naval uniforms.[1] Typically made from animal fiber, the more expensive being of beaver-hair felt and the less expensive of wool felt, the hat's most distinguishing characteristic was that three sides of the brim were turned up (cocked) and either pinned, laced or buttoned in place to form a triangle around the crown.",
        image="Hat.jpg",
        materials="Beaver Fur",
        dimensions="5 3/8 x 13 1/2 x 13 1/4 in.",
        distance="Unknown",
        collection="LACMA",
        link="https://en.wikipedia.org/wiki/Tricorne#/media/File:Tricorne_hat_beaver_fur_c._1780.png",
        page="287",
        department="Outerwear",
        pounds="22s",
        dollars="Unknown",
        license="Public Domain"),

    "Mitts":LedgerItem(
        title="Women's Mitts",
        description="Black silk velvet women's mits. These fingerless mitts lace up the side with tasseled strings and are ornamented with patterns of grey dots.",
        image="Mitts.jpg",
        materials="Silk Velvet",
        dimensions="Length: 8 3/4 in.",
        distance="Unknown",
        collection="LACMA",
        link="http://collections.lacma.org/node/247917",
        page="339",
        department="Outerwear",
        pounds="1s, 2d",
        dollars="Unknown",
        license="Public Domain"),

    "Fan":LedgerItem(
        title="Ivory Fan",
        description="A handheld fan is an implement used to induce an airflow for the purpose of cooling or refreshing oneself. Any broad, flat surface waved back-and-forth will create a small airflow and therefore can be considered a rudimentary fan. Generally, purpose-made handheld fans are shaped like a sector of a circle and made of a thin material (such as paper or feathers) mounted on slats which revolve around a pivot so that it can be closed when not in use.",
        image="Fan.jpg",
        materials="Ivory sticks, mother-of-pearl button",
        dimensions="Length of guard: 11 1/2 in.; Spread: 21 in.",
        distance="3,607 mi",
        collection="LACMA",
        link="http://collections.lacma.org/node/249816",
        page="30",
        department="Accessories",
        pounds="3s, 10d",
        dollars="Unknown",
        license="Public Domain",
        artifact="Folding fan with a gouache landscape painting",
        date="1760",
        origin="England",
        customer="Captain Lewis Ellzey",
        ledger="FanLedger.jpg",
        analytics="There are five fans in the database ranging from 6 pence to 4 shillings 6 pence for an ivory form fan."),

    "Handkerchief":LedgerItem(
        title="Handkerchief",
        description="A handkerchief, also called a handkercher or hanky, is a form of a kerchief, typically a hemmed square of thin fabric that can be carried in the pocket or purse, and which is intended for personal hygiene purposes such as wiping one's hands or face, or blowing one's nose. A handkerchief is also sometimes used as a purely decorative accessory in a suit pocket.",
        image="Handkerchief.jpg",
        materials="Linen, cotton embroidery",
        dimensions="13 3/8 x 13 1/2 in. ",
        distance="6,271 km",
        collection="LACMA",
        link="http://collections.lacma.org/node/235849",
        page="35",
        department="Accessories",
        pounds="12d",
        dollars="Unknown",
        license="Public Domain",
        artifact="Plain weave handkerchief",
        date="circa 1780",
        origin="France",
        customer="John Gist",
        ledger="HandkerchiefLedger.jpg",
        analytics="There are 53 handkerchiefs in the database in an assortment of materials including cotton, linen, silk and lawn. The prices range from 9 shillings for a cotton romall handkerchief, to 4 shillings for a fine lawn handkerchief."),

    "Boots":LedgerItem(
        title="Men's Riding Boots",
        description="Riding boots of black and brown leather",
        image="Boots.jpg",
        materials="Leather, Silver Nails",
        dimensions="18 x 10 1/2 in.",
        distance="Unknown",
        collection="LACMA",
        link="http://collections.lacma.org/node/235713",
        page="353",
        department="Footwear",
        pounds="1 pound, 1s, 6d",
        dollars="Unknown",
        license="Public Domain"),}

def extract_departments(db):
    return set([entry.department for entry in db.values()])

