document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.post-image');

    images.forEach(img => {
        img.style.cursor = 'pointer';
        img.addEventListener('click', () => {
            const modal = document.createElement('div');
            modal.style.position = 'fixed';
            modal.style.top = 0;
            modal.style.left = 0;
            modal.style.width = '100%';
            modal.style.height = '100%';
            modal.style.background = 'rgba(0,0,0,0.8)';
            modal.style.display = 'flex';
            modal.style.alignItems = 'center';
            modal.style.justifyContent = 'center';
            modal.style.zIndex = 1000;

            const modalImg = document.createElement('img');
            modalImg.src = img.src;
            modalImg.style.maxWidth = '90%';
            modalImg.style.maxHeight = '90%';
            modalImg.style.borderRadius = '10px';
            modal.appendChild(modalImg);

            modal.addEventListener('click', () => modal.remove());
            document.body.appendChild(modal);
        });
    });
});
