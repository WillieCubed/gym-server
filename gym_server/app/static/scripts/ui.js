/**
 * Shows the experiment creation dialog.
 */
function showCreateExperimentDialog() {
    // TODO(ui): add is-clipped modifier to a containing element (usually html) to stop scroll overflow.
    // See https://bulma.io/documentation/components/modal/
    console.log('Showing creation dialog');
    document.getElementById('createExperimentDialog').classList.add('is-active');
}

function registerConfigUploadUpdater() {
    // From https://bulma.io/documentation/form/file/
    const fileInput = document.querySelector('#experiment-config-input input[type=file]');
    fileInput.onchange = () => {
        if (fileInput.files.length > 0) {
            const fileName = document.querySelector('#file-js-example .file-name');
            fileName.textContent = fileInput.files[0].name;
        }
    }
}

/**
 * Hide the experiment creation dialog.
 */
function hideCreateExperimentDialog() {
    document.getElementById('createExperimentDialog').classList.remove('is-active');

}