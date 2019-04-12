module.exports = {
    // removeFileExt,
    // cosineSimilarity,
    // euclideanSimilarity,
    // b64toBlob
};

// def remove_file_ext(filename):
//     return os.path.splitext(filename)[0]


// def cosine_similarity(v1, v2):
//     return dot(v1, v2) / (norm(v1) * norm(v2))


// def euclidean_similarity(v1, v2):
//     return norm(v1 - v2)

// function b64toBlob(b64Data, contentType = '', sliceSize = 512) {
//     const byteCharacters = atob(b64Data);
//     const byteArrays = [];

//     for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
//         const slice = byteCharacters.slice(offset, offset + sliceSize);

//         const byteNumbers = new Array(slice.length);
//         for (let i = 0; i < slice.length; i++) {
//             byteNumbers[i] = slice.charCodeAt(i);
//         }

//         const byteArray = new Uint8Array(byteNumbers);
//         byteArrays.push(byteArray);
//     }

//     const blob = new Blob(byteArrays, { type: contentType });
//     return blob;
// }