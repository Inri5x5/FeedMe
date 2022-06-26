const backendServer = `http://localhost:5000`;

// General API-call boilerplate function
const APICall = (requestBody, path, methodType, headersData) => {
    if (requestBody !== null) requestBody = JSON.stringify(requestBody);
    return new Promise((resolve, reject) => {
      const init = {
        method: methodType,
        headers: headersData,
        body: requestBody,
      }
      fetch(`${path}`, init)
        .then(response => {
          if (response.status === 200) {
            return response.json().then(resolve);
          } else if (response.status === 400) {
            return response.json().then(obj => {
              reject(obj.error);
            });
          } else {
            throw new Error(`${response.status} Error with API call`);
          }
        });
    })
  }
  
export { APICall };