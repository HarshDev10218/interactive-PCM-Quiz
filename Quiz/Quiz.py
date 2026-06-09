import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), 'Quiz.db')


def setup_database():
    """Connects to SQLite, creates the quiz table with a subject field, and adds PCM questions."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Rebuild the quiz table so the latest question set is always available.
    cursor.execute("DROP TABLE IF EXISTS quiz_questions")

    # 1. Create the current table schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    
    # 2. Add the quiz questions
    intermediate_questions = [
            # MATHEMATICS (Calculus, Matrices, Vectors)
            ("Math", "What is the derivative of sin(x) with respect to x?", "cos(x)", "-sin(x)", "-cos(x)", "tan(x)", "A"),
            ("Math", "If a matrix A has a determinant of 0, it is called a:", "Identity Matrix", "Singular Matrix", "Symmetric Matrix", "Orthogonal Matrix", "B"),
            ("Math", "What is the value of the definite integral of 2x from 0 to 3?", "6", "9", "12", "3", "B"),
            ("Math", "What is the derivative of e^x with respect to x?", "ln(x)", "e^x", "1/x", "x e^(x-1)", "B"),
            ("Math", "What is the integral of e^x with respect to x?", "ln(x)", "1/x", "e^x + C", "e^(x+1)", "C"),
            ("Math", "If A and B are independent events, what is P(A and B)?", "P(A) + P(B)", "P(A) / P(B)", "P(A) x P(B)", "P(A) - P(B)", "C"),
            ("Math", "What is the dot product of two perpendicular vectors?", "1", "-1", "Infinity", "0", "D"),
            ("Math", "What is the cross product of two parallel vectors?", "The zero vector", "A unit vector", "The vector itself", "Cannot be determined", "A"),
            ("Math", "What is the fundamental period of sin(x)?", "pi", "2*pi", "pi/2", "4*pi", "B"),
            ("Math", "The roots of the quadratic equation ax^2 + bx + c = 0 are given by?", "(-b + sqrt(b^2 - 4ac)) / 2a", "(-b - sqrt(b^2 - 4ac)) / 2a", "Both A and B", "None of these", "C"),
            ("Math", "What are the eigenvalues of an identity matrix?", "0", "1", "-1", "Depends on size", "B"),
            ("Math", "What is the eccentricity of a circle?", "0", "1", "Greater than 1", "Less than 1", "A"),
            ("Math", "What is the eccentricity of an ellipse?", "e = 0", "e = 1", "e > 1", "0 < e < 1", "D"),
            ("Math", "Derivative of tan(x) with respect to x is?", "sec(x)tan(x)", "sec^2(x)", "-csc^2(x)", "cot(x)", "B"),
            ("Math", "What is the sum of the first n natural numbers?", "n(n+1)/2", "n(n+1)(2n+1)/6", "n^2", "(n(n+1)/2)^2", "A"),
            ("Math", "A set with n elements has how many subsets?", "n", "2n", "2^n", "n^2", "C"),
            ("Math", "For any square matrix A, A + A^T is a?", "Symmetric matrix", "Skew-symmetric matrix", "Identity matrix", "Diagonal matrix", "A"),
            ("Math", "For any square matrix A, A - A^T is a?", "Symmetric matrix", "Skew-symmetric matrix", "Identity matrix", "Diagonal matrix", "B"),
            ("Math", "What is the modulus of the complex number 3 + 4i?", "3", "4", "5", "7", "C"),
            ("Math", "What is the principal argument of the complex number 1 + i?", "pi/2", "pi/4", "pi/3", "pi", "B"),
            ("Math", "The line y = mx + c touches the circle x^2 + y^2 = a^2 if c^2 equals?", "a^2 / m^2", "a^2 (1 + m^2)", "a^2 / (1 + m^2)", "a^2 (1 - m^2)", "B"),
            ("Math", "What is the degree of the differential equation d^2y/dx^2 + (dy/dx)^3 = 0?", "1", "2", "3", "Not defined", "A"),
            ("Math", "What is the order of the differential equation d^2y/dx^2 + (dy/dx)^3 = 0?", "1", "2", "3", "4", "B"),
            ("Math", "What is the value of log_e(1)?", "1", "e", "0", "Infinity", "C"),
            ("Math", "What is the value of log_e(e)?", "1", "0", "e", "Infinity", "A"),
            ("Math", "The area bounded by curve y = f(x) and x-axis from x=a to x=b is?", "int_a^b f(x) dx", "int_a^b x dy", "int_a^b f'(x) dx", "None of these", "A"),
            ("Math", "The n-th term of a geometric progression (GP) with first term a and common ratio r is?", "ar", "ar^n", "ar^(n-1)", "a + (n-1)r", "C"),
            ("Math", "The probability of an impossible event is?", "1", "0", "0.5", "Between 0 and 1", "B"),
            ("Math", "The probability of a sure event is?", "0", "0.5", "1", "2", "C"),
            ("Math", "For an invertible matrix A, (A^(-1))^(-1) is equal to?", "A^(-1)", "A", "I", "0", "B"),
            ("Math", "The conjugate of the complex number z = a + ib is?", "a + ib", "a - ib", "-a + ib", "-a - ib", "B"),
            ("Math", "The slope of the tangent to a curve at any point is given by?", "dy/dx", "d^2y/dx^2", "int y dx", "int x dy", "A"),
            ("Math", "The angle theta between two non-zero vectors a and b is given by cos(theta) = ?", "|a x b| / (|a||b|)", "(a . b) / (|a||b|)", "|a . b|", "|a| / |b|", "B"),
            
            # PHYSICS (Mechanics, Thermodynamics, Electrostatics)
            ("Physics", "What is the escape velocity from the surface of the Earth?", "11.2 km/s", "9.8 km/s", "4.2 km/s", "11.2 m/s", "A"),
            ("Physics", "Which law of thermodynamics defines the concept of temperature?", "Zeroth Law", "First Law", "Second Law", "Third Law", "A"),
            ("Physics", "The magnetic field inside a long, straight current-carrying solenoid is:", "Zero", "Decreases near the ends", "Same at all points", "Increases near the ends", "C"),
            ("Physics", "What is the SI unit of force?", "Joule", "Pascal", "Newton", "Watt", "C"),
            ("Physics", "The dimensional formula of force is?", "[MLT^-2]", "[ML^2T^-2]", "[ML^-1T^-2]", "[MLT^-1]", "A"),
            ("Physics", "Work done by a conservative force in a closed loop is?", "Positive", "Negative", "Zero", "Depends on the path", "C"),
            ("Physics", "Kepler's second law (law of areas) is a consequence of the conservation of?", "Linear momentum", "Angular momentum", "Energy", "Charge", "B"),
            ("Physics", "The value of acceleration due to gravity (g) at the center of the Earth is?", "9.8 m/s^2", "Zero", "Infinity", "4.9 m/s^2", "B"),
            ("Physics", "What is the SI unit of electric charge?", "Volt", "Ampere", "Coulomb", "Ohm", "C"),
            ("Physics", "Ohm's law is represented by which equation?", "V = I/R", "V = IR", "P = IV", "R = IV", "B"),
            ("Physics", "Refractive index of a medium with respect to vacuum is given by n = c/v, where v is?", "Speed of light in vacuum", "Frequency of light", "Speed of light in the medium", "Wavelength", "C"),
            ("Physics", "The focal length of a concave mirror is taken as?", "Positive", "Negative", "Zero", "Infinity", "B"),
            ("Physics", "The half-life of a radioactive substance is inversely proportional to its?", "Atomic number", "Mass number", "Decay constant", "Initial quantity", "C"),
            ("Physics", "The de Broglie wavelength of a particle of momentum p is given by?", "lambda = h * p", "lambda = h / p", "lambda = p / h", "lambda = h^2 / p", "B"),
            ("Physics", "The photoelectric effect establishes the?", "Wave nature of light", "Particle nature of light", "Transverse nature of light", "Longitudinal nature of light", "B"),
            ("Physics", "Young's double-slit experiment primarily demonstrates the?", "Particle nature of light", "Wave nature of light", "Electromagnetic nature of light", "Rectilinear propagation", "B"),
            ("Physics", "Lenz's law is a consequence of the law of conservation of?", "Mass", "Charge", "Momentum", "Energy", "D"),
            ("Physics", "The SI unit of magnetic flux is?", "Tesla", "Weber", "Henry", "Gauss", "B"),
            ("Physics", "The dimensional formula of Planck's constant (h) is identical to that of?", "Angular momentum", "Linear momentum", "Force", "Power", "A"),
            ("Physics", "The escape velocity of a body from the Earth's surface does not depend on?", "Mass of the Earth", "Radius of the Earth", "Mass of the body", "Acceleration due to gravity", "C"),
            ("Physics", "For an adiabatic process of an ideal gas, which relation holds true?", "PV = constant", "P/V = constant", "PV^gamma = constant", "P^gamma V = constant", "C"),
            ("Physics", "According to the kinetic theory of gases, the pressure of an ideal gas is?", "1/3 * rho * v^2", "2/3 * rho * v^2", "1/2 * rho * v^2", "rho * v", "A"),
            ("Physics", "Terminal velocity of a small sphere falling through a viscous fluid is proportional to?", "Radius of the sphere", "Square of the radius of the sphere", "Cube of the radius", "Fourth power of radius", "A"),
            ("Physics", "Bernoulli's equation is a statement of the law of conservation of?", "Mass", "Momentum", "Angular momentum", "Energy", "D"),
            ("Physics", "In an isothermal process involving an ideal gas, the change in internal energy is?", "Positive", "Negative", "Zero", "Maximum", "C"),
            ("Physics", "The time period of a simple pendulum depends on?", "Mass of the bob", "Amplitude of oscillation", "Length of the pendulum", "Both mass and length", "C"),
            ("Physics", "The minimum velocity required to project a body away from a gravitational field permanently is?", "Orbital velocity", "Terminal velocity", "Escape velocity", "Threshold velocity", "C"),
            ("Physics", "Coulomb's law for electrostatic force is very similar in form to?", "Newton's first law", "Newton's law of gravitation", "Archimedes' principle", "Hooke's law", "B"),
            ("Physics", "The SI unit of magnetic field induction is?", "Weber", "Tesla", "Henry", "Ampere", "B"),
            ("Physics", "When light travels from an optically rarer medium to a denser medium, it bends?", "Away from the normal", "Towards the normal", "Undeviated", "Parallel to the interface", "B"),
            ("Physics", "A p-n junction diode offers very low resistance when?", "Reverse biased", "Forward biased", "Unbiased", "Saturated", "B"),
            ("Physics", "The energy equivalent of 1 atomic mass unit (amu) is approximately?", "1 MeV", "931.5 MeV", "100 MeV", "9.31 MeV", "B"),
            ("Physics", "How does the surface tension of a liquid change with an increase in temperature?", "Increases", "Decreases", "Remains constant", "First increases then decreases", "B"),

            # CHEMISTRY (Physical, Organic, Inorganic)
            ("Chemistry", "What is the oxidation state of Chromium in K2Cr2O7?", "+3", "+5", "+6", "+7", "C"),
            ("Chemistry", "Which functional group is present in aldehydes?", "-OH", "-CHO", "-COOH", "-CO-", "B"),
            ("Chemistry", "According to the ideal gas equation, what remains constant in an isothermal process?", "Volume", "Pressure", "Temperature", "Number of moles only", "C"),
            ("Chemistry", "What is the pH of a neutral aqueous solution at 298 K?", "0", "7", "14", "Depends on concentration", "B"),
            ("Chemistry", "The chemical formula of gypsum is?", "CaSO4 * 1/2 H2O", "CaSO4 * 2 H2O", "MgSO4 * 7 H2O", "CaCO3", "B"),
            ("Chemistry", "What is the hybridization of carbon in methane (CH4)?", "sp", "sp2", "sp3", "sp3d", "C"),
            ("Chemistry", "What is the hybridization of carbon in ethene (C2H4)?", "sp", "sp2", "sp3", "sp3d", "B"),
            ("Chemistry", "What is the hybridization of terminal carbon in ethyne (C2H2)?", "sp", "sp2", "sp3", "sp3d", "A"),
            ("Chemistry", "Number of moles of solute dissolved per liter of solution is called?", "Molality", "Molarity", "Normality", "Mole fraction", "B"),
            ("Chemistry", "Which of the following elements is liquid at room temperature?", "Bromine", "Mercury", "Both A and B", "Gallium", "C"),
            ("Chemistry", "Which element is the most electronegative in the periodic table?", "Oxygen", "Fluorine", "Chlorine", "Nitrogen", "B"),
            ("Chemistry", "What is the oxidation state of oxygen in hydrogen peroxide (H2O2)?", "-2", "-1", "0", "+1", "B"),
            ("Chemistry", "What is the IUPAC name of acetic acid?", "Methanoic acid", "Ethanoic acid", "Propanoic acid", "Butanoic acid", "B"),
            ("Chemistry", "The functional group >C=O corresponds to which class of organic compounds?", "Alcohols", "Aldehydes", "Ketones", "Ethers", "C"),
            ("Chemistry", "Benzene typically undergoes which type of reactions?", "Electrophilic addition", "Nucleophilic substitution", "Electrophilic substitution", "Free radical addition", "C"),
            ("Chemistry", "According to Lewis theory, an acid is an?", "Electron pair donor", "Proton donor", "Electron pair acceptor", "Proton acceptor", "C"),
            ("Chemistry", "According to Lewis theory, a base is an?", "Electron pair donor", "Proton donor", "Electron pair acceptor", "Proton acceptor", "A"),
            ("Chemistry", "What is the geometry of SF6 molecule?", "Tetrahedral", "Trigonal bipyramidal", "Octahedral", "Square planar", "C"),
            ("Chemistry", "What is the shape of the ammonia (NH3) molecule?", "Trigonal planar", "Tetrahedral", "Pyramidal", "T-shaped", "C"),
            ("Chemistry", "The number of atoms per unit cell in a face-centered cubic (FCC) crystal is?", "1", "2", "4", "6", "C"),
            ("Chemistry", "During the electrolysis of aqueous NaCl, which gas is liberated at the cathode?", "Chlorine gas", "Oxygen gas", "Hydrogen gas", "Sodium vapor", "C"),
            ("Chemistry", "When an active metal reacts with a dilute acid, which gas is usually evolved?", "Oxygen", "Nitrogen", "Hydrogen", "Carbon dioxide", "C"),
            ("Chemistry", "Which catalyst is used in the Haber process for the manufacture of ammonia?", "Finely divided iron", "Platinum", "Nickel", "Vanadium pentoxide", "A"),
            ("Chemistry", "Natural rubber is a polymer of?", "Neoprene", "Isoprene", "Butadiene", "Styrene", "B"),
            ("Chemistry", "Teflon is a polymer of which monomer?", "Ethylene", "Tetrafluoroethylene", "Vinyl chloride", "Propylene", "B"),
            ("Chemistry", "The packing efficiency of a simple cubic unit cell is approximately?", "52.4%", "68%", "74%", "48%", "A"),
            ("Chemistry", "The packing efficiency of a body-centered cubic (BCC) unit cell is approximately?", "52.4%", "68%", "74%", "34%", "B"),
            ("Chemistry", "The packing efficiency of a face-centered cubic (FCC) unit cell is approximately?", "52.4%", "68%", "74%", "48%", "C"),
            ("Chemistry", "What is the conjugate base of water (H2O)?", "H3O+", "OH-", "O2-", "H2", "B"),
            ("Chemistry", "What is the conjugate acid of ammonia (NH3)?", "NH2-", "NH4+", "NO3-", "N2H4", "B"),
            ("Chemistry", "An ideal gas perfectly obeys the gas laws under?", "High pressure and low temperature", "High pressure and high temperature", "Low pressure and high temperature", "All conditions", "C"),
            ("Chemistry", "The law of constant proportions was stated by?", "Antoine Lavoisier", "John Dalton", "Joseph Proust", "Amedeo Avogadro", "C"),
            ("Chemistry", "What is the shape of a water molecule (H2O)?", "Linear", "Bent / V-shaped", "Trigonal planar", "Tetrahedral", "B")
        ]
        
    cursor.executemany('''
        INSERT INTO quiz_questions (subject, question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', intermediate_questions)
    conn.commit()
    print("Database initialized with the latest quiz questions.\n")

    conn.close()

def run_quiz():
    """Allows user to pick a subject and pulls random questions using SQLite."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("=== INTERMEDIATE LEVEL QUIZ CHANNELS ===")
    print("1. Mathematics")
    print("2. Physics")
    print("3. Chemistry")
    print("4. Mixed (All Subjects)")

    # Validate menu choice
    choice = input("\nChoose a topic (1-4): ").strip()
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please select 1-4.")
        conn.close()
        return
    
    # Validate and get number of questions
    while True:
        try:
            count_input = input("How many questions do you want? (default: 3): ").strip()
            count = int(count_input) if count_input else 3
            
            if count < 1 or count > 10:
                print("Please enter a number between 1 and 10.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Define query filter based on selection
    if choice == "1":
        cursor.execute("SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM quiz_questions WHERE subject='Math' ORDER BY RANDOM() LIMIT ?", (count,))
        print("\n--- Math Quiz Starting ---\n")
    elif choice == "2":
        cursor.execute("SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM quiz_questions WHERE subject='Physics' ORDER BY RANDOM() LIMIT ?", (count,))
        print("\n--- Physics Quiz Starting ---\n")
    elif choice == "3":
        cursor.execute("SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM quiz_questions WHERE subject='Chemistry' ORDER BY RANDOM() LIMIT ?", (count,))
        print("\n--- Chemistry Quiz Starting ---\n")
    else:
        cursor.execute("SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM quiz_questions ORDER BY RANDOM() LIMIT ?", (count,))
        print("\n--- Grand Mixed Quiz Starting ---\n")
        
    questions = cursor.fetchall()
    conn.close()
    
    if not questions:
        print("No questions found.")
        return

    score = 0
    questions_answered = 0
    total = len(questions)
    
    print("Type A, B, C, or D to answer. Type 'q' to quit.\n")
    
    for index, row in enumerate(questions, start=1):
        question, opt_a, opt_b, opt_c, opt_d, correct = row
        
        print(f"Q{index}: {question}")
        print(f"  A) {opt_a}")
        print(f"  B) {opt_b}")
        print(f"  C) {opt_c}")
        print(f"  D) {opt_d}")
        
        # Validate user answer
        while True:
            user_answer = input("Your answer: ").strip().upper()
            
            if user_answer == 'Q':
                print("\nExiting quiz early...\n")
                questions_answered = index - 1
                break
            elif user_answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Please enter A, B, C, D, or Q to quit.")
        
        if user_answer == 'Q':
            break
        
        questions_answered = index
        
        if user_answer == correct:
            print("✓ Correct! Excellent.\n")
            score += 1
        else:
            print(f"✗ Incorrect. The correct choice was {correct}.\n")
            
    # Display final scoreboard
    print("=" * 50)
    print("=== FINAL SCOREBOARD ===")
    print("=" * 50)
    
    if questions_answered > 0:
        percentage = (score / questions_answered) * 100
        print(f"Final Score: {score}/{questions_answered} ({percentage:.1f}%)")
        
        # Performance feedback
        if percentage == 100:
            print("🏆 Perfect Score! Outstanding!")
        elif percentage >= 80:
            print("🌟 Excellent Performance!")
        elif percentage >= 60:
            print("👍 Good Job! Keep Practicing!")
        else:
            print("💪 Keep Practicing! You'll do better next time!")
    else:
        print("No questions answered.")
    
    print("=" * 50)

if __name__ == "__main__":
    setup_database()
    run_quiz()
