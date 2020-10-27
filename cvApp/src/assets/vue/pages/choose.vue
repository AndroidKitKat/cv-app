// Require Cordova plugin : cordova-plugin-camera

<template>
  <f7-page>
      <f7-navbar title="Choose" back-link="Back"></f7-navbar>
      <img style="width: 100%" v-if="imagePath !== ''" :src="imagePath" />
      <f7-button class="button-outline-ios" @click="takePicture">{{ btnTitle }}</f7-button>
      <f7-button class="button-outline-ios" @click="sendPicture" v-if="btnTitle === 'Choose different photo'">Submit</f7-button>
            <f7-button class="button-outline-ios" @click="netcall" v-if="btnTitle === 'Choose different photo'">Submit</f7-button>

      {{ dater }}
  </f7-page>
</template>
<script>
import { nativeAlert } from "../../libs/index";

export default {
  components: {},
  data() {
    return {
      imagePath: "",
      btnTitle: "Choose photo",
      dater: ""
    };
  },
  methods: {
    takePicture: function () {
      if (navigator.camera) {
        navigator.camera.getPicture(this.setPicture, this.error, {
          destinationType: Camera.DestinationType.DATA_URL,
          sourceType: Camera.PictureSourceType.PHOTOLIBRARY,
        });
      } else {
        // If the navigator.camera is not available display generic error to the user.
        this.error();
      }
    },
    setPicture: function(imageData) {
      this.imagePath = "data:image/jpeg;base64," + imageData
      this.btnTitle = "Choose different photo"
    },
    error: function() {
      nativeAlert("this is the sad");
    },
    sendPicture: function() {

fetch('http://10.18.16.48:9090/test.txt').then(res=>res.text()).then(data=>nativeAlert(data))

// 1. Create a new XMLHttpRequest object
    // let xhr = new XMLHttpRequest();

    // // 2. Configure it: GET-request for the URL /article/.../load
    // xhr.open('GET', 'https://waifupaste.moe/raw/nOK.txt');

    // // 3. Send the request over the network
    // xhr.send();

    // // 4. This will be called after the response is received
    // xhr.onload = function() {
    //   if (xhr.status != 200) { // analyze HTTP status of the response
    //     nativeAlert(`Error ${xhr.status}: ${xhr.statusText}`); // e.g. 404: Not Found
    //   } else { // show the result
    //     nativeAlert(`Done, got ${xhr.response.length} bytes`); // response is the server
    //   }
    // };

    // xhr.onprogress = function(event) {
    //   if (event.lengthComputable) {
    //     nativeAlert(`Received ${event.loaded} of ${event.total} bytes`);
    //   } else {
    //     nativeAlert(`Received ${event.loaded} bytes`); // no Content-Length
    //   }

    // };

    // xhr.onerror = function() {
    //   this.dater = xhr
    //   nativeAlert('poop')
    // };
    },
  // lifecycle hooks
  }
}
</script>