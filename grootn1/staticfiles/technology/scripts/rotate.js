document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector(".carousel");
    let isDragging = false;
    let startX, startRotation = 0;

    carousel.addEventListener("mousedown", (e) => {
        isDragging = true;
        startX = e.clientX;
        startRotation = getRotationY(carousel);
    });

    document.addEventListener("mousemove", (e) => {
        if (isDragging) {
            let deltaX = e.clientX - startX;
            carousel.style.transform = `rotateY(${startRotation + deltaX * 0.5}deg)`;
        }
    });

    document.addEventListener("mouseup", () => {
        isDragging = false;
    });

    function getRotationY(el) {
        let transform = window.getComputedStyle(el).getPropertyValue("transform");
        if (transform !== "none") {
            let values = transform.split("(")[1].split(")")[0].split(",");
            let a = values[0], b = values[2];
            let angle = Math.round(Math.atan2(b, a) * (180 / Math.PI));
            return angle;
        }
        return 0;
    }
});
