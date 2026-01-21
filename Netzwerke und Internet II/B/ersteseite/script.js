const canvas = document.getElementById('snowCanvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const flockenAnzahl = 100;
const groesse = 3; // Alle Flocken sind 3 Pixel groß
const flocken = [];

// Flocken erstellen
for (let i = 0; i < flockenAnzahl; i++) {
    flocken.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        speed: Math.random() * 2 + 1 // Unterschiedliche Geschwindigkeit für Tiefe
    });
}

function zeichnen() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "white";

    for (let i = 0; i < flockenAnzahl; i++) {
        let f = flocken[i];

        // Kreis zeichnen
        ctx.beginPath();
        ctx.arc(f.x, f.y, groesse, 0, Math.PI * 2);
        ctx.fill();

        // Bewegung
        f.y += f.speed;

        // Reset am oberen Rand
        if (f.y > canvas.height) {
            f.y = -groesse;
            f.x = Math.random() * canvas.width;
        }
    }
    requestAnimationFrame(zeichnen);
}

zeichnen();