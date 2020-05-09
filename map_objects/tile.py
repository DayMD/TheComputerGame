class Tile:
    #a map tile, may be blocked and may block sight

    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        if block_sight is None:
            block_sight = blocked
        
        self.block_sight = block_sight