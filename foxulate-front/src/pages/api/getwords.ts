// export const config = {
//   api: {
//     bodyParser: false, // Defaults to true. Setting this to false disables body parsing and allows you to consume the request body as stream or raw-body.
//     responseLimit: false, // Determines how much data should be sent from the response body. It is automatically enabled and defaults to 4mb.
//     externalResolver: true, // Disables warnings for unresolved requests if the route is being handled by an external resolver like Express.js or Connect. Defaults to false.
//   },
// }

import { NextApiRequest, NextApiResponse } from "next";
import NextCors from 'nextjs-cors'

export default async function handler(req:NextApiRequest, res:NextApiResponse) {
   // Run the cors middleware
   // nextjs-cors uses the cors package, so we invite you to check the documentation https://github.com/expressjs/cors
   await NextCors(req, res, {
      // Options
      methods: ['GET', 'HEAD', 'PUT', 'PATCH', 'POST', 'DELETE'],
      origin: '*',
      optionsSuccessStatus: 200, // some legacy browsers (IE11, various SmartTVs) choke on 204
   });

  //  console.log(req.body)
   const response = fetch('http://127.0.0.1:5000/getWordsFromScenario', {body:JSON.stringify(req.body), method:'POST', headers:{
 "Accept": "*/*",
 "Content-Type": "text/plain"
}})
 let data = await response;
  let json = await data.json();

   // Rest of the API logic
   res.send(json);
}
