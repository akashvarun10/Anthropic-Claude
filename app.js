import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic({
    apiKey: "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", // defaults to process.env["ANTHROPIC_API_KEY"]
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
