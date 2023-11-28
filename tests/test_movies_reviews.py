# Internal modules
from main import get_movies_review


def init_movies_reviews() -> str:
    """Initialise the movies' reviews.
    """
    # initialisation
    test_movie_title = "The Matrix"
    return get_movies_review(test_movie_title)


def test_type_get_movies_review():
    """Test the type of the function get_movies_review.
    """
    # initialisation
    movies_reviews = init_movies_reviews()

    # check if the result is a string, since JSON is returned as a string in Python
    assert isinstance(
        movies_reviews, str), "The function should return a string."


def test_content_get_movies_review():
    """Test the function get_movies_review.
    """
    # initialisation
    movies_reviews = init_movies_reviews()

    # test
    assert movies_reviews == "[{\"0\":\"Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.\"},{\"0\":\"Plagued by strange memories, Neo's life takes an unexpected turn when he finds himself back inside the Matrix.\"},{\"0\":\"Six months after the events depicted in The Matrix, Neo has proved to be a good omen for the free humans, as more and more humans are being freed from the matrix and brought to Zion, the one and only stronghold of the Resistance.  Neo himself has discovered his superpowers including super speed, ability to see the codes of the things inside the matrix and a certain degree of pre-cognition. But a nasty piece of news hits the human resistance: 250,000 machine sentinels are digging to Zion and would reach them in 72 hours. As Zion prepares for the ultimate war, Neo, Morpheus and Trinity are advised by the Oracle to find the Keymaker who would help them reach the Source.  Meanwhile Neo's recurrent dreams depicting Trinity's death have got him worried and as if it was not enough, Agent Smith has somehow escaped deletion, has become more powerful than before and has fixed Neo as his next target.\"},{\"0\":\"The human city of Zion defends itself against the massive invasion of the machines as Neo fights to end the war at another front while also opposing the rogue Agent Smith.\"},{\"0\":\"The film goes behind the scenes of the 1999 sci-fi movie The Matrix.\"},{\"0\":\"The making of Matrix Revolutions, The (2003) is briefly touched on here in this documentary. Interviews with various cast and crew members inform us how they were affected by the deaths of Gloria Foster and Aaliyah, and also delve into the making of the visual effects that takes up a lot of screen time. Written by Rhyl Donnelly\"},{\"0\":\"The making of The Matrix Revolutions:  The cataclysmic final confrontation chronicled through six documentary pods revealing 28 featurettes\"},{\"0\":\"Are we in fact living in a simulation? This is the question postulated, wrestled with, and ultimately argued for through archival footage, compelling interviews with real people shrouded in digital avatars, and a collection of cases from some of our most iconoclastic figures in contemporary culture.\"},{\"0\":\"A promotional making-of documentary for the film Matrix, The (1999) that devotes its time to explaining the digital and practical effects contained in the film. This is very interesting, seeing as how they're giving away the cinematic secrets that they created solely for the this movie, that have now been spoofed and referenced in countless other films.\"},{\"0\":\"The making of The Matrix Reloaded:  Go to the middle movie's furthest reaches via five documentary paths revealing 21 featurettes.\"},{\"0\":\"This making-of piece offers the standard mix of movie snippets, behind the scenes materials, and interviews from cast and crew on the making of the film.\"},{\"0\":\"Disc 8 of 10 of 'The Matrix: Ultimate Edition': Probe the philosophical and technological inspirations of The Matrix Trilogy through two insightful documentaries:  - Return to Source: Philosophy &amp; The Matrix documentary \\u2013 Scholars, philosophers and theorists deconstruct the intellectual underpinnings of the trilogy  - The Hard Problem: The Science Behind the Fiction documentary \\u2013 Is the notion of a real Matrix plausible? An investigation of the technologies that inspire the metaphor of the Matrix.\"},{\"0\":\"Special Effects wizard John Gaeta demonstrates how the \\\"Bullet-Time\\\" effects were created for the film Matrix, The (1999).\"},{\"0\":\"A featurette about the special effects of The Matrix Trilogy\"},{\"0\":\"A look at Enter the Matrix: The game's story picks up just before The Matrix Reloaded and runs parallel to that of the film. Bend the rules of the Matrix with martial arts, pilot the fastest hovercraft in the fleet, or just fight with lots of guns.\"},{\"0\":\"An hour long discussion on the philosophical concepts that inspired, and are presented in the trilogy. This is one of the two feature-length documentaries on disc number 8 of the 10-Disc Ultimate Set.\"},{\"0\":\"This thirty-minute documentary follows the Wachowski sisters and the film's crew through production on the film's famed highway chase sequence. We get interviews with the visual effects supervisors, the stunt coordinators and even are taken through aspects of pre-production and planning for the scene. Then the documentary moves into production, the scariest aspect of which is certainly Carrie Anne-Moss trying to learn to ride a motorcycle good enough to do so safely without helmet for the scene. We also watch as the stretch of freeway used in the film is being built.\"},{\"0\":\"In a world of lies and deception and false hopes, the time is now to remove the blinders of deception and take back our lives.\"},{\"0\":\"A look at the stunts of The Matrix Revolutions\"},{\"0\":\"The special effects of the Agent Smith scenes in Matrix Revolutions\"}]"
