
class Stage:
    _actor = None

    @staticmethod
    def set_the_stage(actor):
        Stage._actor = actor
        #print(f"🎬 {actor.get_name()} entra al escenario")

    @staticmethod
    def the_actor_in_the_spotlight():
        return Stage._actor

    @staticmethod
    def clear_the_stage():
        Stage._actor = None