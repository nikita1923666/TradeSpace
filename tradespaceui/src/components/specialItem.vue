<template>
    <div id="myitem">
        <div class="text-center">
            <v-dialog
                    v-model="dialog"
                    width="800"
            >
                <template v-slot:activator="{ on }">
                    <v-card v-bind:style="[selected ? {'background':'green'} : {'background':'white'}]"
                            class="mx-auto"
                            max-width="344"
                            v-on="on"
                    >
                        <v-list-item>
                            <p id="text"> {{ itemTitle }}</p>
                        </v-list-item>
                    </v-card>
                </template>

                <v-card>
                    <v-card-title
                            class="headline grey lighten-2"
                            primary-title
                            style="display: block"
                    >
                        <v-row>
                            <v-col>
                                <v-list-item-title
                                        style="display: inline-block; font-size: 40px; margin-top:20px; margin-left: 10px">
                                    {{itemTitle}}
                                </v-list-item-title>
                            </v-col>
                        </v-row>
                    </v-card-title>

                    <v-card-text style="padding: 1% 5% 1% 5%">
                        <v-row>
                            <v-col>
                                <b-card-img v-bind:src="itemPhoto" class="rounded-0"
                                            style="width:350px; height:350px"></b-card-img>
                            </v-col>
                            <v-col>
                                {{itemDescription}}
                            </v-col>
                        </v-row>
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" v-if="notEditMode" @click="select">Select</v-btn>

                        <v-btn text color="primary" v-if="editMode"
                               @click="$router.push({path: `/editItem/${itemID}`})">Edit Item
                        </v-btn>
                        <v-btn
                                color="primary"
                                text
                                @click="dialog = false"
                        >
                            Back
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>
    </div>
</template>

<script>

    import firebase from 'firebase';
    import axios from 'axios';

    export default {
        name: 'Item',
        //DO PROP VALIDATION IF THERE IS TIME: https://vuejs.org/v2/guide/components-props.html
        props: [
            'item',
            'tradeId'
            //Item contains an array with all the different components
        ],
        data: () => ({
            itemTitle: '',
            itemDescription: '',
            itemPhoto: '',
            itemTags: '',
            itemLocation: '',
            owner_uid: '',
            itemID: '',
            itemOwnerID: '',
            name: '',
            profilePhoto: '',
            dialog: false,
            editMode: false,
            notEditMode: true,
            selected: false,
            tradeID: ''
        }),
        methods: {
            select: function () {
                this.$store.commit('selectItem', this.itemID);
                this.dialog = false;
                this.selected = true;
            }
        },
        created() {
            this.itemTitle = this.item['title'];
            this.itemDescription = this.item['description'];
            this.itemPhoto = this.item['photo_url'];
            this.itemTags = this.item['tags'];
            this.itemLocation = this.item['location'];
            this.itemID = this.item['item_id'];
            this.owner_uid = this.item['owner_uid'];
            this.tradeID = this.tradeId;
            let self = this;
            if (this.owner_uid !== null || this.owner_uid !== '') {
                axios.get('/users/' + self.owner_uid, {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'token ' + self.$store.getters.authToken
                    }
                })
                    .then(response => {
                        let user = response.data;
                        self.name = user['display_name'];
                    });

                    self.photo_path = self.itemPhoto.split('appspot.com/')[1];
                    var storage = firebase.storage();
                    var storageRef = storage.ref();
                    storageRef.child(self.photo_path).getDownloadURL().then(function (url) {
                        self.itemPhoto = url;
                    });
            }
        }

    }
    ;
</script>

<style scoped>
    #myitem {
        margin: 5px;
        display: inline-block;
    }

    #text {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-height: 100px;
    }
</style>
