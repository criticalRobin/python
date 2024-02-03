def how_many_bees(hive):
    bees = 0
    
    for row in hive:
        bees += row.count("bee")
        bees += row.count("eeb")
    
    rotated_hive = ["".join(row) for row in zip(*hive[::-1])]

    for row in rotated_hive:
        bees += row.count("bee")
        bees += row.count("eeb")

    return bees
        
    
            

example = [
".eb.bb.beee...e.eeeebe..bee",
"e.eebeb.ebe.e.ee..bbee..be.",
".b.e..eebebee.eeeeeb..b.e.b",
".ebbbbbee.eeeee...e.e..eb.e",
".e..eb.e.ebe.eb.ebbeeeee.b.",
"beeebbeb.e...b.b..eeee..eee",
"bbe.beb.be.eeeeb.ee..ee.e..",
"bbee..e...be.eb.ebee.eeeb.e",
"eeee..eeb.e.b..eeb..ebbbee.",
"beeb.ebee.e.e..ee.ebbe.b..e",
"e.beee.ebeeb....ebb..ebe.ee",
"e.eb.b.e.b...be.eeeebee.bee",
".eeb..ee.ee.eeb...beebe.bbe",
"...b.beebe.ebbeee..b.eee.ee",
"...ebe.beeebee.e..e.be.ebbe",
".b..eebe.eb.be.b.e.bee.eeee",
"be.ebbe..eebe..b...eeebe.ee",
"eeb.bbeb..bee.ee.beeee....e",
"beebbee.e.e.e..beb.eee.eb..",
"eeb.be.e.e..be.e..e.ebeebeb",
"..eb.bbbeeebe.ee.b..eeee..e",
"b.eeeb.e...bbeee.e.eb.e.bee",
"e..e.ebee..e..eebeebe.b.ebb",
".ebeeee.bebeeee.....bb.ebe.",
"..ebe.beeeb.be.eebe...ee.eb",
".be.eb.be.e..ee.bbee.eebe.e",
".b.bbebeeb.eee.e.eee.eb..e."
]

print(how_many_bees(example))