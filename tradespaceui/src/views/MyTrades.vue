<template>
  <b-container fluid style="padding: 80px 40px 0 40px">
    <b-card
      class="overflow-hidden"
      style="margin-top: 10px"
      v-for="trade in trade_list"
      v-bind:key="trade.seller_item_id"
    >
      <b-row>
        <b-col>
          <b-card-img :src="itemImage" class="rounded-0"></b-card-img>
        </b-col>
        <b-col>
          <v-list-item>
            <v-list-item-avatar color="grey">
              <v-img :src="avatar"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title class="headline">
                {{ itemTitle }}
              </v-list-item-title>
              <router-link :to="name">
                <v-list-item-subtitle>by {{ name }}</v-list-item-subtitle>
              </router-link>
              <v-list-item-subtitle>{{ location }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <b-card-body title="">
            <b-card-text>
              {{ description }}
            </b-card-text>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card>
  </b-container>
</template>

<script>
export default {
  name: "MyTrades",
  components: {},
  data: () => ({
    trade_list: [
      {
        buyer_id: "54321",
        seller_id: "12345",
        buyer_item_id: null,
        seller_item_id: "33322",
        type: null
      },
      {
        buyer_id: "12345",
        seller_id: "44433",
        buyer_item_id: null,
        seller_item_id: "33322",
        type: null
      }
    ]
  })
};
</script>

<style scoped>
.noHyperlink {
  text-decoration: none;
  color: black;
}
</style>
