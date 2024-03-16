import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic({
    apiKey: "", // defaults to process.env["ANTHROPIC_API_KEY"]
  });
  
async function main() {
const result = await client. completions.create({
    prompt:`${Anthropic.HUMAN_PROMPT} Give me a daily meal plan ${Anthropic.AI_PROMPT}`,
    model: "claude-2.1" ,
    stream: true,
    max_tokens_to_sample: 300,
}) ;
for await(const completion of result){
  process.stdout.write(completion.completion);
}
}

main (). catch((err) => {
console.error(err);
process.exit(1);
});
