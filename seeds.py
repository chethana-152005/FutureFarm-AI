seeds = {
"Rice": ["MTU 1010", "IR64", "Swarna"],
"Wheat": ["HD2967", "PBW550"],
"Cotton": ["Bunny Bt", "RCH 659"],
"Maize": ["DHM117", "HQPM1"]
}

def get_seeds(crop):

    return seeds.get(crop,"No data")
