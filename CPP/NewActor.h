// -----------------------------------------------------------
// NewActor.h
// v.1.0
// Updated: 20211103
// -----------------------------------------------------------

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"

#include "NewActor.generated.h"

UCLASS()
class SANDBOX_CPP_V4271_API ANewActor : public AActor
{
    GENERATED_BODY()

public:
    // Sets default values for this actor's properties
    ANewActor();

public:
    virtual void OnConstruction();

protected:
    // Called when the game starts or when spawned
    virtual void BeginPlay() override;

public:
    // Called every frame
    virtual void Tick(float DeltaTime) override;

};
