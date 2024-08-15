let fileInputCount = 1;

function addFileInput() {
    fileInputCount++;
    const fileInputsDiv = document.getElementById('file-inputs');
    
    const newFileLabel = document.createElement('label');
    newFileLabel.setAttribute('for', `file${fileInputCount}`);
    newFileLabel.textContent = `Upload file ${fileInputCount}:`;
    
    const newFileInput = document.createElement('input');
    newFileInput.type = 'file';
    newFileInput.id = `file${fileInputCount}`;
    newFileInput.name = 'files';

    // 動的に生成されたファイル入力に対応するプレビュー要素を生成
    const newPreviewElement = document.createElement('div');
    newPreviewElement.id = `previewContainer${fileInputCount}`;
    
    newFileInput.onchange = function() {
        // ファイルの種類に応じてプレビュー要素を作成
        const fileType = newFileInput.files[0].type;
        let previewElement;
        
        if (fileType.startsWith('image/')) {
            previewElement = document.createElement('img');
            previewElement.style = 'max-width: 100%;';
        } else if (fileType.startsWith('video/')) {
            previewElement = document.createElement('video');
            previewElement.controls = true;
            previewElement.style = 'max-width: 200px;';
        } else if (fileType.startsWith('audio/')) {
            previewElement = document.createElement('audio');
            previewElement.controls = true;
        } else if (fileType === 'application/pdf') {
            previewElement = document.createElement('iframe');
            previewElement.style = 'width: 100%; height: 500px;';
        } else {
            alert('このファイル形式はプレビューできません。');
            return;
        }
        
        newPreviewElement.innerHTML = ''; // 既存のプレビューをクリア
        newPreviewElement.appendChild(previewElement);
        preview(newFileInput, previewElement);
    };

    fileInputsDiv.appendChild(newFileLabel);
    fileInputsDiv.appendChild(newFileInput);
    fileInputsDiv.appendChild(newPreviewElement);
}

function preview(input, previewElement) {
    const file = input.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        previewElement.src = e.target.result;
    };

    reader.readAsDataURL(file);
}

function previewPDF(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = (e) => {
            const pdfPreview = document.getElementById('previewPDF');
            pdfPreview.src = e.target.result;  // 修正: src 属性を使用
            pdfPreview.onerror = () => {
                console.error('Error loading PDF');
            };
        };
        reader.onerror = () => {
            console.error('Error reading file');
        };
        reader.readAsDataURL(input.files[0]);
    }
}

  