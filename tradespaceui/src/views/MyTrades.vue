<template>
  <b-container fluid style="padding: 80px 40px 0 40px">
    <b-card
      class="overflow-hidden"
      style="margin-top: 10px;"
      v-for="trade in trade_list"
      v-bind:key="trade.seller_item_id"
    >
      <b-row>
        <b-col>
          <b-card v-if="user_id == trade.buyer_id">
            <b-card-img :src="trade.image_url" class="imageSize"></b-card-img>
            <b-card-text> Buyer Item: {{ trade.buyer_item_id }} </b-card-text>
          </b-card>

          <b-card v-if="user_id == trade.seller_id">
            <b-card-img :src="trade.image_url" class="imageSize"></b-card-img>
            <b-card-text> Seller Item: {{ trade.seller_item_id }} </b-card-text>
          </b-card>
        </b-col>

        <b-col>
          <b-card v-if="user_id == trade.seller_id">
            <b-card-img
              src="https://media.licdn.com/dms/image/C5603AQHN1MngtTdA7Q/profile-displayphoto-shrink_800_800/0?e=1580342400&v=beta&t=mAHZ16NRQ4TAWIxs0NM1Y5YQbw_tc3r3SuQ1bJIx3YI"
              class="imageSize"
            ></b-card-img>
            <b-card-text> Seller: {{ trade.seller_id }} </b-card-text>
          </b-card>

          <b-card v-if="user_id == trade.buyer_id">
            <b-card-img
              src="https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-9/50787743_991195991071591_4988716462626570240_n.jpg?_nc_cat=103&_nc_ohc=UaT26VSYKiwAQmae_is2QZmJDCVGnsPQ4I2xwaSuysQ_5Vs4BxAfiVtQQ&_nc_ht=scontent-lax3-1.xx&oh=6a3f853447276ee9374fcc74fa220b64&oe=5E8784AB"
              class="imageSize"
            >
            </b-card-img>
            <b-card-text> Buyer: {{ trade.buyer_id }} </b-card-text>
          </b-card>
        </b-col>

        <b-col>
          <b-img
            :src="require('@/assets/check.jpg')"
            width="50"
            height="50"
            v-if="user_id == trade.seller_id"
          />
          <b-img
            :src="require('@/assets/pending.png')"
            width="50"
            height="50"
            v-if="user_id == trade.buyer_id"
          />
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
        buyer_id: "nikita54321",
        seller_id: "nikita12345",
        buyer_item_id: null,
        seller_item_id: "item33322",
        type: null,
        image_url:
          "https://cdn.shopify.com/s/files/1/0217/3274/products/pau3053_106_h_large.jpg?v=1543863314"
      },
      {
        buyer_id: "nikita12345",
        seller_id: "nikita44433",
        buyer_item_id: null,
        seller_item_id: "item33322",
        type: null,
        image_url:
          "https://cdn.shopify.com/s/files/1/0128/9452/products/Puffer-Jacket-FIBL09_959f4782-35d5-40e2-95c9-881682dd440d_1024x1024.png?v=1542326918"
      }
    ],
    user_id: "nikita12345"
  })
};
</script>

<style scoped>
.noHyperlink {
  text-decoration: none;
  color: black;
}

.imageSize {
  width: 100%;
  height: 20vw;
  object-fit: cover;
}
</style>
