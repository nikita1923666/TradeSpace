<template>
  <b-container fluid style="padding: 80px 40px 0 40px">
    <div style="padding-bottom: 30px">
      <div class="mt-3">
        Item Image: {{ itemImage ? itemImage.name : "" }}
      </div>
      <br />
      <b-form-file
        v-model="itemImage"
        :state="Boolean(itemImage)"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
        @change="selectImage"
      ></b-form-file>
    </div>

    <b-form-input
      v-model="itemTitle"
      label="Item Title"
      placeholder="Item Title (e.g. Adidas shoes and a green dress)"
      required
    ></b-form-input>

    <b-form-input
      v-model="location"
      label="Location"
      placeholder="Location"
      style="margin-top: 10px"
      required
    ></b-form-input>

    <div style="margin-top: 10px">
      <b-form-input
        v-model="newTag"
        v-on:keyup.enter.native="addTag"
        placeholder="Enter a new tag..."
        style="margin-bottom:15px"
      ></b-form-input>

      <ul>
        <v-btn
          v-on:click="removeTag(tag.name)"
          style="margin-right:20px"
          v-for="tag in tags"
          v-bind:key="tag.name"
          >{{ tag.name }}</v-btn
        >
      </ul>
    </div>

    <div>
      <b-form-textarea
        id="textarea"
        v-model="description"
        placeholder="Describe your item..."
        rows="3"
        max-rows="6"
      ></b-form-textarea>
    </div>

    <div style="padding: 10px">
      <v-btn large color="primary" @click="addItem">Add Item</v-btn>
      <router-link to="/account">
        <v-btn large style="margin-left: 30px" color="secondary"> Cancel </v-btn>
      </router-link>
    </div>

    <div class="text-center ma-2">
            <v-snackbar
                    v-model="snackbar"
            >
                {{ text }}
                <v-btn
                        color="pink"
                        text
                        @click="snackbar = false"
                >
                    Close
                </v-btn>
            </v-snackbar>
        </div>

  </b-container>
</template>

<script>


import firebase from 'firebase';
import axios from 'axios';
import qs from 'querystring';


export default {
  data: () => ({
    location: "",
    name: "Nikita",
    itemTitle: "",
    tags: [],
    itemImage: null,
    newTag: "",
    imageData: null,
    description: "",
    user_id: "",
    text: '',
    snackbar: false,
  }),

  methods: {
    successUpload() {
      this.$vs.notify({
        color: "success",
        title: "Upload Success",
        text: "Upload Suceeded"
      });
    },
    addTag() {
      this.tags.push({ name: this.newTag });
      this.newTag = "";
    },
    removeTag(tagToRemove) {
      this.tags = this.tags.filter(item => item.name != tagToRemove);
    },
    selectImage: function(file) {
      this.itemImage = file;
    },
    addItem() {
      let self = this;
      // console.log("title: " + self.itemTitle);
      // console.log("location: " + self.location);
      // console.log("description: " + self.description);
      // upload the photo and get url
      var storage_ref = firebase.storage().ref();
      var auth_token = self.$store.getters.authToken
      axios.get('/users/', {
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
              'Authorization': 'token ' + auth_token
          }
      })
          .then(response => {
              let userInfo = response.data;
              self.user_id = userInfo['user_id']
              var image_path = self.user_id + "/" + self.itemTitle
              var profile_ref = storage_ref.child(image_path)
              const profile_metadata = { contentType: self.itemImage.type }
              profile_ref.put(self.itemImage, profile_metadata);
              var photo_url = "gs://tradespace-22f37.appspot.com/" + image_path;
              self.uploadItem(auth_token, photo_url);
          })
          .catch(error => {
              let errorCode = error.code;
              let errorMessage = error.message;
              self.snackbar = true;
              self.text = "ERROR " + errorCode + ":" + errorMessage;
          });
    },
    uploadItem: function(auth_token, photo_url) {
        let self = this;

        var tags_arr = [];
        var i;
        for (i = 0; i < self.tags.length; i++) {
          tags_arr.push(self.tags[i].name);
        }

        axios.post('/items/', qs.stringify({
            'title': self.itemTitle,
            'location': self.location,
            'description': self.description,
            'tags': tags_arr,
            'photo_url': photo_url
        }), {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'token ' + auth_token
            }
        })
            .then(response => {
                self.snackbar = true;
                self.text = "Successfully Uploaded Item: " + response['data']['title'];
                //Get back an Item variable. Not sure if the information is needed, but it is not used.
                self.$router.replace('account');
            })
            .catch(error => {
                let errorCode = error.code;
                let errorMessage = error.message;
                self.snackbar = true;
                self.text = "ERROR " + errorCode + ":" + errorMessage;
            });
    }
  }
};
</script>

<style scoped>
.dropbox {
  outline: 2px dashed grey; /* the dash box */
  outline-offset: -10px;
  background: lightcyan;
  color: dimgray;
  padding: 10px 10px;
  min-height: 200px; /* minimum height */
  position: relative;
  cursor: pointer;
}

.input-file {
  opacity: 0; /* invisible but it's there! */
  width: 100%;
  height: 200px;
  position: absolute;
  cursor: pointer;
}

.dropbox:hover {
  background: lightblue; /* when mouse over to the drop zone, change color */
}

.dropbox p {
  font-size: 1.2em;
  text-align: center;
  padding: 50px 0;
}
</style>
